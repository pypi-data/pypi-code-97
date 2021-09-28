# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Quantiles(Model):
    """Numerical quantiles.

    :param p0_d1: Represents 1% quantile.
    :type p0_d1: float
    :param p1: Represents 1% quantile.
    :type p1: float
    :param p5: Represents 5% quantile.
    :type p5: float
    :param p25: Represents 25% quantile.
    :type p25: float
    :param p50: Represents 50% quantile.
    :type p50: float
    :param p75: Represents 75% quantile.
    :type p75: float
    :param p95: Represents 95% quantile.
    :type p95: float
    :param p99: Represents 99% quantile.
    :type p99: float
    :param p99_d9: Represents 9% quantile.
    :type p99_d9: float
    """

    _attribute_map = {
        'p0_d1': {'key': 'p0D1', 'type': 'float'},
        'p1': {'key': 'p1', 'type': 'float'},
        'p5': {'key': 'p5', 'type': 'float'},
        'p25': {'key': 'p25', 'type': 'float'},
        'p50': {'key': 'p50', 'type': 'float'},
        'p75': {'key': 'p75', 'type': 'float'},
        'p95': {'key': 'p95', 'type': 'float'},
        'p99': {'key': 'p99', 'type': 'float'},
        'p99_d9': {'key': 'p99D9', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(Quantiles, self).__init__(**kwargs)
        self.p0_d1 = kwargs.get('p0_d1', None)
        self.p1 = kwargs.get('p1', None)
        self.p5 = kwargs.get('p5', None)
        self.p25 = kwargs.get('p25', None)
        self.p50 = kwargs.get('p50', None)
        self.p75 = kwargs.get('p75', None)
        self.p95 = kwargs.get('p95', None)
        self.p99 = kwargs.get('p99', None)
        self.p99_d9 = kwargs.get('p99_d9', None)
