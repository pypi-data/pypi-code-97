import logging
import datetime
import six

logger = logging.getLogger('urbanairship')


class Unauthorized(Exception):
    """Raised when we get a 401 from the server"""


class AirshipFailure(Exception):
    """Raised when we get an error response from the server.

    :param args: For backwards compatibility, ``*args`` includes the status and
        response body.

    """

    error = None
    error_code = None
    details = None
    response = None

    def __init__(self, error, error_code, details, response, *args):
        self.error = error
        self.error_code = error_code
        self.details = details
        self.response = response
        super(AirshipFailure, self).__init__(*args)

    @classmethod
    def from_response(cls, response):
        """
        Instantiate a ValidationFailure from a Response object
        :param response: response object used to create failure obj
        """
        try:
            payload = response.json()
            error = payload.get('error')
            error_code = payload.get('error_code')
            details = payload.get('details')
        except (ValueError, TypeError, KeyError):
            error = response.reason
            error_code = response.status_code
            details = response.content

        logger.warning(
            "Request failed with status %d: '%s %s': %s",
            response.status_code, error_code, error, details)

        return cls(
            error,
            error_code,
            details,
            response,
            response.status_code,
            response.content
        )


@six.python_2_unicode_compatible
class IteratorDataObj(object):
    @classmethod
    def from_payload(cls, payload, device_key=None, airship=None):
        obj = cls()
        if device_key:
            obj.device_type = device_key
        if device_key and payload[device_key]:
            obj.id = payload[device_key]
        if airship:
            obj.airship = airship
        for key in payload:
            try:
                val = datetime.datetime.strptime(
                    payload[key],
                    '%Y-%m-%d %H:%M:%S'
                )
            except (TypeError, ValueError):
                val = payload[key]
            setattr(obj, key, val)
        return obj

    def __str__(self):
        print_str = ""
        for attr in dir(self):
            if(
                not attr.startswith('__') and
                not hasattr(getattr(self, attr), '__call__')
            ):
                print_str += attr + ': ' + str(getattr(self, attr)) + ', '
        return print_str[:-2]


class IteratorParent(six.Iterator):
    next_url = None
    data_attribute = None
    data_list = None
    params = None
    id_key = None
    instance_class = IteratorDataObj

    def __init__(self, airship, params):
        self.airship = airship
        self.params = params
        self._token_iter = iter(())

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.instance_class.from_payload(
                next(self._token_iter),
                self.id_key,
                self.airship
            )
        except StopIteration:
            if self._load_page():
                return self.instance_class.from_payload(
                    next(self._token_iter),
                    self.id_key,
                    self.airship
                )
            else:
                raise StopIteration

    def _load_page(self):
        if not self.next_url:
            return False
        response = self.airship.request(
            method='GET',
            body=None,
            url=self.next_url,
            version=3,
            params=self.params
        )
        self.params = None
        self._page = response.json()
        check_url = self._page.get('next_page')
        if check_url == self.next_url:
            return False
        self.next_url = check_url
        self._token_iter = iter(self._page[self.data_attribute])
        return True
