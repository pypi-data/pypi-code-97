from unittest import mock
from urllib.parse import quote_plus

from django.test import TestCase, RequestFactory
from django.test.utils import override_settings

from globus_portal_framework.tests import get_mock_data, mocks

from globus_portal_framework.gsearch import (
    post_search, get_index, get_pagination, get_filters,
    process_search_data, get_facets, get_search_filters,
    get_date_range_for_date, get_search_query, parse_filters,
    prepare_search_facets, serialize_gsearch_range, deserialize_gsearch_range,
    get_field_facet_filter_types,
)
from globus_portal_framework.exc import (
    IndexNotFound, GlobusPortalException, InvalidRangeFilter,
)
from globus_portal_framework.constants import FILTER_MATCH_ALL

MOCK_RESULTS = 'globus_portal_framework/tests/data/search.json'


class MockSearchGetSubject:
    data = {'content': [{'myindex': 'search_data'}]}


class MockSearchAPI500Error(Exception):
    http_status = 500


class MockSearchAPI400Error(Exception):
    http_status = 400


class MockGlobusResponse:
    def __init__(self):
        self.data = {}


MOCK_FACETS = {
    "facet_results": [
        {
            "@datatype": "GFacetResult",
            "@version": "2017-09-01",
            "buckets": [
                {
                    "@datatype": "GBucket",
                    "@version": "2017-09-01",
                    "count": 99,
                    "value": "Problems"
                }
            ],
            "name": "Things I Got"
        }
    ],
}

MOCK_PORTAL_DEFINED_FACETS = [{
    'name': 'Things I Got',
    'type': 'terms',
    'field_name': 'things.i.got',
    'size': 10
}]


class SearchUtilsTest(TestCase):

    SEARCH_INDEXES = {'myindex': {
        # Randomly generated and not real
        'uuid': '1e0be00f-8156-499e-980d-f7fb26157c02'
    }}

    def setUp(self):
        self.factory = RequestFactory()

    @override_settings(SEARCH_INDEXES={'foo': {}})
    def test_get_index(self):
        self.assertEqual(get_index('foo'), {})

    @override_settings(SEARCH_INDEXES={'foo': {'uuid': 'foo_uuid'}})
    def test_post_search_invalid_args(self):
        empty = {'search_results': [], 'facets': []}
        assert post_search(None, '*', [], user=None, page=1) == empty
        assert post_search('foo', None, [], user=None, page=1) == empty

    @override_settings(SEARCH_INDEXES={'foo': {'uuid': 'foo_uuid'}})
    @mock.patch('globus_sdk.SearchClient.post_search')
    def test_post_search_basic(self, gs_post_search):
        mock_search = MockGlobusResponse()
        mock_search.data = mocks.MOCK_EMPTY_SEARCH
        gs_post_search.return_value = mock_search
        post_search('foo', '*', [], user=None, page=1)
        assert gs_post_search.called

    @override_settings(SEARCH_INDEXES={'foo': {'uuid': 'foo_uuid'}})
    @mock.patch('globus_sdk.exc.SearchAPIError', MockSearchAPI500Error)
    @mock.patch('globus_sdk.SearchClient.post_search')
    def test_post_search_search_500_error(self, gs_post_search):
        gs_post_search.side_effect = MockSearchAPI500Error
        result = post_search('foo', '*', [], user=None, page=1)
        assert 'error' in result

    @override_settings(SEARCH_INDEXES={'foo': {'uuid': 'foo_uuid'}})
    @mock.patch('globus_sdk.exc.SearchAPIError', MockSearchAPI400Error)
    @mock.patch('globus_sdk.SearchClient.post_search')
    def test_post_search_dgpf_error(self, gs_post_search):
        gs_post_search.side_effect = MockSearchAPI400Error
        result = post_search('foo', '*', [], user=None, page=1)
        assert 'error' in result

    @override_settings(SEARCH_INDEXES={})
    def test_get_index_raises_error_on_nonexistent_index(self):
        with self.assertRaises(IndexNotFound):
            get_index('foo')

    def test_process_search_data_with_no_records(self):
        mappers, results = [], []
        data = process_search_data(mappers, results)
        self.assertEqual(data, [])

    @mock.patch('globus_portal_framework.gsearch.log')
    def test_process_search_data_zero_length_content(self, log):
        sub = get_mock_data(MOCK_RESULTS)['gmeta'][0]
        sub['content'] = []
        mappers, results = [], [sub]
        data = process_search_data(mappers, results)
        self.assertEqual(log.warning.call_count, 1)
        self.assertEqual(data, [])

    def test_process_search_data_with_one_entry(self):
        sub = get_mock_data(MOCK_RESULTS)['gmeta'][0]
        mappers, results = [], [sub]
        data = process_search_data(mappers, results)[0]
        self.assertEqual(quote_plus(sub['subject']), data['subject'])
        self.assertEqual(sub['content'], data['all'])

    def test_process_search_data_string_field(self):
        sub = get_mock_data(MOCK_RESULTS)['gmeta'][0]
        sub['content'][0]['foo'] = 'bar'
        mappers, results = ['foo'], [sub]
        data = process_search_data(mappers, results)[0]
        self.assertEqual(data['foo'], 'bar')

    def test_process_search_data_func_field(self):
        sub = get_mock_data(MOCK_RESULTS)['gmeta'][0]
        sub['content'][0]['foo'] = 'bar'
        mappers = [('foo', lambda x: x[0].get('foo').replace('b', 'c'))]
        results = [sub]
        data = process_search_data(mappers, results)[0]
        self.assertEqual(data['foo'], 'car')

    def test_process_search_data_string_field_missing(self):
        sub = get_mock_data(MOCK_RESULTS)['gmeta'][0]
        sub['content'][0]['foo'] = 'bar'
        mappers, results = ['foo'], [sub]
        data = process_search_data(mappers, results)[0]
        self.assertEqual(data['foo'], 'bar')

    @override_settings(RESULTS_PER_PAGE=10, MAX_PAGES=10)
    def test_pagination(self):
        self.assertEqual(get_pagination(1000, 0)['current_page'], 1)
        self.assertEqual(get_pagination(1000, 10)['current_page'], 2)
        self.assertEqual(get_pagination(1000, 20)['current_page'], 3)
        self.assertEqual(len(get_pagination(1000, 0)['pages']), 10)

    @mock.patch('globus_portal_framework.gsearch.log.warning')
    @override_settings(DEFAULT_FILTER_MATCH=FILTER_MATCH_ALL)
    def test_get_filters(self, warning):
        r = get_filters({'titles': ['foo']})
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0]['type'], 'match_all')

        r = get_filters({'titles': ['foo', 'bar']})
        self.assertEqual(len(r), 1)
        self.assertTrue(warning.called)

    @override_settings(DEFAULT_FILTER_MATCH=FILTER_MATCH_ALL,
                       SEARCH_INDEX={'foo': {'uuid': 'bar'}})
    def test_get_search_filters(self):
        # list of tests urls and expected outputdicts
        filter_tests = [
            ('/?q=*&filter.foo=bar', [{
                'field_name': 'foo',
                'type': 'match_all',
                'values': ['bar']}]
             ),
            ('/?q=*&filter-match-any.foo=bar', [{
                'field_name': 'foo',
                'type': 'match_any',
                'values': ['bar']}]
             ),
            ('/?q=*&filter-match-all.foo=bar', [{
                'field_name': 'foo',
                'type': 'match_all',
                'values': ['bar']}]
             ),
            ('/?q=*&page=1&filter-year.foo=2018', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': '2018-01-01 00:00:00',
                            'to': '2019-01-01 00:00:00'}]}]
             ),
            ('/?q=*&page=1&filter-month.foo=2018-01', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': '2018-01-01 00:00:00',
                            'to': '2018-01-31 00:00:00'}]}]
             ),
            ('/?q=*&page=1&filter-day.foo=2018-08-13', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': '2018-08-13 00:00:00',
                            'to': '2018-08-14 00:00:00'}]}]
             ),
            ('/?q=*&page=1&filter-day.foo=2018-08-13+12:50:03', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': '2018-08-13 00:00:00',
                            'to': '2018-08-14 00:00:00'}]}]
             ),
            ('/?q=*&page=1&filter-hour.foo=2018-02-27+23:31:07', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': '2018-02-27 23:00:00',
                            'to': '2018-02-27 23:59:59'}]}]
             ),
            ('/?q=*&page=1&filter-minute.foo=2018-03-28+23:31:07', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': '2018-03-28 23:31:00',
                            'to': '2018-03-28 23:31:59'}]}]
             ),
            ('/?q=*&page=1&filter-second.foo=2018-03-28+23:31:07', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': '2018-03-28 23:31:06',
                            'to': '2018-03-28 23:31:08'}]}]
             ),
            ('/?q=*&filter-range.foo=1--2', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': 1, 'to': 2}]}]
             ),
            ('/?q=*&filter-range.foo=1.5--2.9', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': 1.5, 'to': 2.9}]}]
             ),
            ('/?q=*&page=1&filter-range.foo=100--*', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': 100, 'to': '*'}]}]
             ),
            ('/?q=*&page=1&filter-range.foo=100--*', [{
                'field_name': 'foo',
                'type': 'range',
                'values': [{'from': 100, 'to': '*'}]}]
             ),
        ]
        for query, expected_result in filter_tests:
            r = self.factory.get(query)
            filters = get_search_filters(r)
            self.assertEqual(filters, expected_result)

    def test_get_search_query(self):
        r = self.factory.get('/?q=coffee+and+chocolate')
        self.assertEqual(get_search_query(r), 'coffee and chocolate')

    def test_get_facets(self):
        search_response = MockGlobusResponse()
        search_response.data = MOCK_FACETS
        r = get_facets(search_response, MOCK_PORTAL_DEFINED_FACETS, {})
        self.assertEqual(len(r), 1)
        facet = r[0]
        self.assertEqual(set(facet.keys()), {'name', 'buckets'})
        bucket = facet['buckets'][0]
        self.assertEqual(set(bucket.keys()), {'count', 'value', 'field_name',
                                              'checked', 'filter_type',
                                              'search_filter_query_key'})
        # No filters defined in third argument, this should not be 'checked'
        self.assertFalse(bucket['checked'])

    @override_settings(DEFAULT_FILTER_MATCH=FILTER_MATCH_ALL)
    def test_checked_facet_shows_up(self):
        search_response = MockGlobusResponse()
        search_response.data = MOCK_FACETS
        request = self.factory.get('/?filter.things.i.got=Problems')
        filters = get_search_filters(request)
        r = get_facets(search_response, MOCK_PORTAL_DEFINED_FACETS, filters)
        self.assertTrue(r[0]['buckets'][0]['checked'])

    def test_get_invalid_search_range_raises_error(self):
        with self.assertRaises(GlobusPortalException):
            get_date_range_for_date('2018-02-02', 'fortnight')
        with self.assertRaises(InvalidRangeFilter):
            get_date_range_for_date('not a valid date', 'day')

    def test_parse_valid_term_filter(self):
        tfilters = ['application/x-hdf', 'image/png']
        assert parse_filters(tfilters, 'filter_match_all') == tfilters

        tfilters = ['application/x-hdf', 'image/png']
        assert parse_filters(tfilters, 'filter_match_any') == tfilters

    def test_parse_valid_range_filters(self):
        valid_filters = (
            (['2019-10-25 16:43:00'], 'day'),
            (['2019-10-25 16:43:00--2019-10-25 16:43:00'], 'range'),
            (['1--100'], 'range'),
        )
        for rfilter, filter_type in valid_filters:
            search = parse_filters(rfilter, filter_type)
            self.assertEqual(len(search), 1)
            assert set(search[0].keys()) == {'from', 'to'}

    @mock.patch('globus_portal_framework.gsearch.log.debug')
    def test_invalid_range_filters(self, log):
        parse_filters(['not_a_valid_range'], 'range')
        self.assertTrue(log.called)

    def test_prepare_search_facets_valid(self):
        self.assertEqual(prepare_search_facets([{
                'field_name': 'foo.bar.baz'
            }]),
            [{
                'field_name': 'foo.bar.baz',
                'name': 'foo.bar.baz',
                'type': 'terms',
                'size': 10
            }]
        )

    def test_prepare_search_facets_extra_items(self):
        self.assertEqual(prepare_search_facets([{
                'field_name': 'foo.bar.baz',
                'thick_but_beloved_superheroes': 'The Tick'
            }]),
            [{
                'field_name': 'foo.bar.baz',
                'name': 'foo.bar.baz',
                'type': 'terms',
                'size': 10
            }]
        )

    def test_prepare_search_facets_invalid(self):
        # Invalid, should be list of dicts
        with self.assertRaises(ValueError):
            prepare_search_facets({'field_name': 'foo'})
        # invalid, should at least define 'field_name'
        with self.assertRaises(ValueError):
            prepare_search_facets([{}])

    def test_serialize_gserach_range(self):
        self.assertEqual(
            serialize_gsearch_range({'from': 'min_value', 'to': 'max_value'}),
            'min_value--max_value'
        )
        self.assertEqual(
            serialize_gsearch_range({'from': 0, 'to': 10}), '0--10'
        )

    def test_deserialize_gsearch_range(self):
        with self.assertRaises(InvalidRangeFilter):
            deserialize_gsearch_range('no-separator-in-range')
        with self.assertRaises(InvalidRangeFilter):
            deserialize_gsearch_range('--missing-low-bounds')
        with self.assertRaises(InvalidRangeFilter):
            deserialize_gsearch_range('missing-high-bounds--')

    def test_get_field_facet_filter_types_valid(self):
        facets = get_field_facet_filter_types([
            {'field_name': 'foo.defaults.to.terms'},
            {'field_name': 'foo.match-all', 'filter_type': 'match-all'},
            {'field_name': 'foo.match-any', 'filter_type': 'match-any'},
            {'field_name': 'foo.num.hist', 'type': 'numeric_histogram'},
            {'field_name': 'foo.date.hist', 'type': 'date_histogram',
             'date_interval': 'day'},
        ])
        self.assertEqual(facets['foo.defaults.to.terms'], 'match-all')
        self.assertEqual(facets['foo.match-all'], 'match-all')
        self.assertEqual(facets['foo.match-any'], 'match-any')
        self.assertEqual(facets['foo.num.hist'], 'range')
        self.assertEqual(facets['foo.date.hist'], 'day')

    def test_get_field_facet_filter_types_invalid_filter(self):
        with self.assertRaises(ValueError):
            get_field_facet_filter_types([{'field_name': 'foo', 'type': ''}])
