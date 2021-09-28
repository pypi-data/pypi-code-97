from dateutil.parser import parse

from django.test import TestCase
from atws.wrapper import Wrapper

import random
from copy import deepcopy
from djautotask import models
from djautotask import sync, sync_rest
from djautotask.utils import DjautotaskSettings
from djautotask.tests import fixtures, mocks, fixture_utils


class AssertSyncMixin:

    def assert_sync_job(self):
        qset = \
            models.SyncJob.objects.filter(
                entity_name=self.model_class.__bases__[0].__name__
            )
        assert qset.exists()


class SynchronizerRestTestMixin(AssertSyncMixin):
    synchronizer_class = None
    model_class = None
    fixture = None
    update_field = None
    lookup_key = 'id'

    def setUp(self):
        super().setUp()
        self.fixture_items = self.fixture["items"]

    def _call_api(self, return_data):
        raise NotImplementedError

    def _assert_fields(self, instance, json_data):
        raise NotImplementedError

    def _sync(self, return_data):
        _, get_patch = self._call_api(return_data)
        self.synchronizer = self.synchronizer_class()
        self.synchronizer.sync()
        return _, get_patch

    def _sync_with_results(self, return_data):
        _, get_patch = self._call_api(return_data)
        self.synchronizer = self.synchronizer_class()
        return self.synchronizer.sync()

    def _parse_datetime(self, datetime):
        return parse(datetime) if datetime else None

    def test_sync(self):
        self._sync(self.fixture)
        instance_dict = {
            int(c[self.lookup_key]): c for c in self.fixture_items
        }

        for instance in self.model_class.objects.all():
            json_data = instance_dict[instance.id]
            self._assert_fields(instance, json_data)

        self.assert_sync_job()

    def test_save_instace(self):
        """
        Test to ensure synchronizer saves a instance locally.
        """
        self.assertGreater(self.model_class.objects.all().count(), 0)

        object_data = self.fixture_items[0]
        instance = self.model_class.objects.get(
            id=object_data[self.lookup_key]
        )

        self._assert_fields(instance, object_data)
        self.assert_sync_job()

    def test_sync_update(self):
        self._sync(self.fixture)

        json_data = self.fixture_items[0]

        instance_id = json_data[self.lookup_key]
        original = self.model_class.objects.get(id=instance_id)

        new_val = None
        update_field_type = type(getattr(original, self.update_field))
        if update_field_type is str:
            new_val = 'Some New Value'
        elif update_field_type is bool:
            new_val = not getattr(original, self.update_field)
        elif update_field_type is int:
            new_val = getattr(original, self.update_field) + 1

        new_json = deepcopy(self.fixture_items[0])
        new_json[self.update_field] = new_val
        new_json_list = [new_json]

        return_value = {
            "items": new_json_list,
            "pageDetails": fixtures.API_PAGE_DETAILS
        }
        self._sync(return_value)

        changed = self.model_class.objects.get(id=instance_id)

        self.assertNotEqual(getattr(original, self.update_field), new_val)
        self._assert_fields(changed, new_json)

    def test_delete_stale_instances(self):
        """
        Local instance should be deleted if not returned during a full sync
        """
        instance_id = self.fixture_items[0][self.lookup_key]
        instance_qset = self.model_class.objects.filter(id=instance_id)
        self.assertEqual(instance_qset.count(), 1)

        _, patch = self._call_api(fixtures.API_EMPTY)

        synchronizer = self.synchronizer_class(full=True)
        synchronizer.sync()
        self.assertEqual(instance_qset.count(), 0)
        patch.stop()

    def test_sync_skips(self):
        self._sync(self.fixture)

        new_val = 'Some New Value'
        new_json = deepcopy(self.fixture_items[0])
        new_json[self.update_field] = new_val
        new_json_list = [new_json]

        # Sync it twice to be sure that the data will be updated, then ignored
        return_value = {
            "items": new_json_list,
            "pageDetails": fixtures.API_PAGE_DETAILS
        }
        self._sync(return_value)
        _, updated_count, skipped_count, _ = \
            self._sync_with_results(return_value)

        self.assertEqual(skipped_count, 1)
        self.assertEqual(updated_count, 0)


class PicklistSynchronizerRestTestMixin(SynchronizerRestTestMixin):
    update_field = 'label'
    lookup_key = 'value'

    def setUp(self):
        self.fixture_items = self.fixture["fields"][0]["picklistValues"]
        self._sync(self.fixture)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, int(object_data['value']))
        self.assertEqual(instance.label, object_data['label'])
        self.assertEqual(instance.is_default_value,
                         object_data['isDefaultValue'])
        self.assertEqual(instance.sort_order, object_data['sortOrder'])
        self.assertEqual(instance.is_active, object_data['isActive'])
        self.assertEqual(instance.is_system, object_data['isSystem'])

    def test_sync_skips(self):
        self._sync(self.fixture)

        new_val = 'Some New Value'
        new_fixture = deepcopy(self.fixture)
        new_json = new_fixture['fields'][0]['picklistValues'][0]
        new_json[self.update_field] = new_val

        # Sync it twice to be sure that the data will be updated, then ignored
        return_value = new_fixture
        self._sync(return_value)
        _, updated_count, skipped_count, _ = \
            self._sync_with_results(return_value)

        self.assertGreater(skipped_count, 0)
        self.assertEqual(updated_count, 0)

    def test_sync_update(self):
        self._sync(self.fixture)

        json_data = self.fixture_items[0]

        instance_id = json_data[self.lookup_key]
        original = self.model_class.objects.get(id=instance_id)

        new_val = 'Some New Value'
        new_fixture = deepcopy(self.fixture)
        new_json = new_fixture['fields'][0]['picklistValues'][0]
        new_json[self.update_field] = new_val
        return_value = new_fixture

        self._sync(return_value)
        changed = self.model_class.objects.get(id=instance_id)

        self.assertNotEqual(getattr(original, self.update_field), new_val)
        self._assert_fields(changed, new_json)


class TestContactSynchronizer(SynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.ContactSynchronizer
    model_class = models.ContactTracker
    fixture = fixtures.API_CONTACT
    update_field = 'phone'

    def setUp(self):
        super().setUp()
        fixture_utils.init_accounts()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_contacts_call(return_data)

    def _assert_fields(self, instance, json_data):
        self.assertEqual(instance.id, json_data['id'])
        self.assertEqual(instance.first_name, json_data['firstName'])
        self.assertEqual(instance.last_name, json_data['lastName'])
        self.assertEqual(instance.email_address, json_data['emailAddress'])
        self.assertEqual(instance.email_address2, json_data['emailAddress2'])
        self.assertEqual(instance.email_address3, json_data['emailAddress3'])
        self.assertEqual(instance.account_id, json_data['companyID'])
        self.assertEqual(instance.phone, json_data['phone'])
        self.assertEqual(instance.alternate_phone, json_data['alternatePhone'])
        self.assertEqual(instance.mobile_phone, json_data['mobilePhone'])


class TestAssignNullRelationMixin:
    def test_sync_assigns_null_relation(self):
        model_type = self.model_class.__bases__[0].__name__
        model_object = self.model_class.objects.first()

        self.assertIsNotNone(model_object.assigned_resource)

        fixture_instance = deepcopy(
            getattr(fixtures, 'API_{}'.format(model_type.upper()))
        )
        fixture_instance['items'][0].pop(self.assign_null_relation_field)

        _, patch = self._call_api(fixture_instance)
        synchronizer = self.synchronizer_class(full=True)
        synchronizer.sync()

        model_object = self.model_class.objects.get(id=model_object.id)
        self.assertIsNone(model_object.assigned_resource)
        patch.stop()


class SynchronizerTestMixin:
    model_class = None
    synchronizer = None
    fixture = None
    update_field = None
    updated_data = 'New Data'

    def _sync(self, return_data):
        query_generator = \
            fixture_utils.generate_objects(
                self.model_class.__bases__[0].__name__, [return_data])
        _, patch = mocks.api_query_call(query_generator)
        return self.synchronizer.sync()

    def test_skips(self):
        updated_instance = deepcopy(self.fixture)
        updated_instance[self.update_field] = self.updated_data

        _, updated_count, skipped_count, _ = self._sync(updated_instance)
        self.assertEqual(updated_count, 1)
        self.assertEqual(skipped_count, 0)

        _, updated_count, skipped_count, _ = self._sync(updated_instance)
        self.assertEqual(skipped_count, 1)
        self.assertEqual(updated_count, 0)

    def assert_sync_job(self):
        qset = models.SyncJob.objects.filter(
            entity_name=self.model_class.__bases__[0].__name__)
        assert qset.exists()


class TestTicketNoteSynchronizer(SynchronizerTestMixin, TestCase):
    model_class = models.TicketNoteTracker
    fixture = fixtures.API_TICKET_NOTE
    update_field = 'Title'

    def setUp(self):
        super().setUp()
        self.synchronizer = sync.TicketNoteSynchronizer()
        mocks.init_api_connection(Wrapper)
        fixture_utils.init_resources()
        fixture_utils.init_tickets()
        fixture_utils.init_note_types()
        fixture_utils.init_ticket_notes()

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.title, object_data['Title'])
        self.assertEqual(instance.description, object_data['Description'])
        self.assertEqual(
            instance.create_date_time, object_data['CreateDateTime'])
        self.assertEqual(
            instance.last_activity_date, object_data['LastActivityDate'])
        self.assertEqual(instance.ticket.id, object_data['TicketID'])
        self.assertEqual(
            instance.creator_resource.id, object_data['CreatorResourceID'])
        self.assertEqual(instance.note_type.id, object_data['NoteType'])

    def test_sync_ticket_note(self):
        """
        Test to ensure note synchronizer saves a TicketNote instance locally.
        """
        self.assertGreater(models.TicketNote.objects.all().count(), 0)

        object_data = fixtures.API_TICKET_NOTE
        instance = models.TicketNote.objects.get(id=object_data['id'])

        self._assert_sync(instance, object_data)
        self.assert_sync_job()

    def test_delete_stale_ticket_notes(self):
        """
        Local notes should be deleted if not returned during a full sync
        """
        note_id = fixtures.API_TICKET_NOTE['id']
        qs = models.TicketNote.objects.filter(id=note_id)
        self.assertEqual(qs.count(), 1)

        mocks.api_query_call([])

        synchronizer = sync.TicketNoteSynchronizer(full=True)
        synchronizer.sync()
        self.assertEqual(qs.count(), 0)


class TestTaskNoteSynchronizer(SynchronizerTestMixin, TestCase):
    model_class = models.TaskNoteTracker
    fixture = fixtures.API_TASK_NOTE
    update_field = 'Title'

    def setUp(self):
        super().setUp()
        self.synchronizer = sync.TaskNoteSynchronizer()
        mocks.init_api_connection(Wrapper)
        fixture_utils.init_resources()
        fixture_utils.init_projects()
        fixture_utils.init_tasks()
        fixture_utils.init_note_types()
        fixture_utils.init_task_notes()

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.title, object_data['Title'])
        self.assertEqual(instance.description, object_data['Description'])
        self.assertEqual(
            instance.create_date_time, object_data['CreateDateTime'])
        self.assertEqual(
            instance.last_activity_date, object_data['LastActivityDate'])
        self.assertEqual(instance.task.id, object_data['TaskID'])
        self.assertEqual(
            instance.creator_resource.id, object_data['CreatorResourceID'])
        self.assertEqual(instance.note_type.id, object_data['NoteType'])

    def test_sync_task_note(self):
        """
        Test to ensure note synchronizer saves a TaskNote instance locally.
        """
        self.assertGreater(models.TaskNote.objects.all().count(), 0)

        object_data = fixtures.API_TASK_NOTE
        instance = models.TaskNote.objects.get(id=object_data['id'])

        self._assert_sync(instance, object_data)
        self.assert_sync_job()

    def test_delete_stale_task_notes(self):
        """
        Local notes should be deleted if not returned during a full sync
        """
        note_id = fixtures.API_TASK_NOTE['id']
        qs = models.TaskNote.objects.filter(id=note_id)
        self.assertEqual(qs.count(), 1)

        mocks.api_query_call([])

        synchronizer = sync.TaskNoteSynchronizer(full=True)
        synchronizer.sync()
        self.assertEqual(qs.count(), 0)


class TestTicketSynchronizer(
        SynchronizerRestTestMixin, TestAssignNullRelationMixin, TestCase):
    synchronizer_class = sync_rest.TicketSynchronizer
    model_class = models.TicketTracker
    fixture = fixtures.API_TICKET
    update_field = 'title'
    assign_null_relation_field = 'assignedResourceID'

    def setUp(self):
        super().setUp()
        fixture_utils.init_contracts()
        fixture_utils.init_statuses()
        fixture_utils.init_resources()
        fixture_utils.init_accounts()
        fixture_utils.init_account_physical_locations()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_tickets_call(return_data)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.title, object_data['title'])
        self.assertEqual(instance.ticket_number, object_data['ticketNumber'])
        self.assertEqual(instance.completed_date,
                         self._parse_datetime(object_data['completedDate']))
        self.assertEqual(instance.create_date,
                         self._parse_datetime(object_data['createDate']))
        self.assertEqual(instance.description, object_data['description'])
        self.assertEqual(instance.due_date_time,
                         self._parse_datetime(object_data['dueDateTime']))
        self.assertEqual(instance.estimated_hours,
                         object_data['estimatedHours'])
        self.assertEqual(instance.last_activity_date,
                         self._parse_datetime(object_data['lastActivityDate']))
        self.assertEqual(instance.status.id, object_data['status'])
        self.assertEqual(instance.assigned_resource.id,
                         object_data['assignedResourceID'])
        self.assertEqual(instance.contract.id, object_data['contractID'])
        self.assertEqual(instance.account.id, object_data['companyID'])
        self.assertEqual(instance.account_physical_location.id,
                         object_data['companyLocationID'])

    def test_sync_ticket_related_records(self):
        """
        Test to ensure that a ticket will sync related objects,
        in its case notes, and time entries, and secondary resources
        """
        ticket = models.Ticket.objects.first()
        ticket.status = models.Status.objects.first()
        time_mock, time_patch = mocks.create_mock_call(
            'djautotask.sync.TimeEntrySynchronizer.fetch_records',
            None
        )
        note_mock, note_patch = mocks.create_mock_call(
            'djautotask.sync.TicketNoteSynchronizer.fetch_records', None)
        resource_mock, resource_patch = mocks.create_mock_call(
            'djautotask.sync.TicketSecondaryResourceSynchronizer.'
            'fetch_records',
            None
        )
        _, _checklist_patch = mocks.create_mock_call(
            "djautotask.sync_rest.TicketChecklistItemsSynchronizer.sync_items",
            None
        )

        self.synchronizer.sync_related(ticket)

        self.assertEqual(time_mock.call_count, 1)
        self.assertEqual(note_mock.call_count, 1)
        self.assertEqual(resource_mock.call_count, 1)
        time_patch.stop()
        note_patch.stop()
        resource_patch.stop()
        _checklist_patch.stop()


class PicklistSynchronizerTestMixin:

    def setUp(self):
        mocks.init_api_connection(Wrapper)

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['Value'])
        self.assertEqual(instance.label, object_data['Label'])
        self.assertEqual(
            instance.is_default_value, object_data['IsDefaultValue'])
        self.assertEqual(instance.sort_order, object_data['SortOrder'])
        self.assertEqual(instance.is_active, object_data['IsActive'])
        self.assertEqual(instance.is_system, object_data['IsSystem'])

    def test_evaluate_sync(self):
        """
        Test to ensure given picklist synchronizer saves its instance locally.
        """
        instance_dict = {}
        for item in self.fixture:
            instance_dict[item['Value']] = item

        for instance in self.model_class.objects.all():
            object_data = instance_dict[instance.id]

            self._assert_sync(instance, object_data)

        self.assert_sync_job()

    def test_evaluate_objects_deleted(self):
        """
        Test that a give object is deleted if not returned during a full sync.
        """
        qset = self.model_class.objects.all()
        self.assertEqual(qset.count(), len(self.fixture))

        # Ensure that the get_field_info method returns no API objects
        # so that the full sync will remove the existing objects in the DB.
        mocks.get_field_info_api_calls()

        synchronizer = self.synchronizer(full=True)
        synchronizer.sync()
        self.assertEqual(qset.count(), 0)

    def _sync(self, return_data):
        picklist_field = self.synchronizer.picklist_field \
            if hasattr(self.synchronizer, 'picklist_field') \
            else self.model_class.__bases__[0].__name__
        query_generator = \
            fixture_utils.generate_picklist_objects(
                picklist_field, [return_data])
        _, patch = mocks.api_picklist_call(query_generator)
        return self.synchronizer().sync()

    def test_skips(self):
        updated_instance = deepcopy(self.fixture[0])
        updated_instance['Label'] = 'New Data'

        _, updated_count, skipped_count, _ = self._sync(updated_instance)
        self.assertEqual(updated_count, 1)
        self.assertEqual(skipped_count, 0)

        _, updated_count, skipped_count, _ = self._sync(updated_instance)
        self.assertEqual(skipped_count, 1)
        self.assertEqual(updated_count, 0)

    def assert_sync_job(self):
        qset = models.SyncJob.objects.filter(
            entity_name=self.model_class.__bases__[0].__name__)
        assert qset.exists()


class TestStatusSynchronizer(PicklistSynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.StatusSynchronizer
    model_class = models.StatusTracker
    fixture = fixtures.API_STATUS_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_ticket_picklist_call(return_data)


class TestPrioritySynchronizer(PicklistSynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.PrioritySynchronizer
    model_class = models.PriorityTracker
    fixture = fixtures.API_PRIORITY_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_ticket_picklist_call(return_data)


class TestQueueSynchronizer(PicklistSynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.QueueSynchronizer
    model_class = models.QueueTracker
    fixture = fixtures.API_QUEUE_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_ticket_picklist_call(return_data)


class TestProjectStatusSynchronizer(PicklistSynchronizerTestMixin, TestCase):
    model_class = models.ProjectStatusTracker
    fixture = fixtures.API_PROJECT_STATUS_LIST
    synchronizer = sync.ProjectStatusSynchronizer

    def setUp(self):
        super().setUp()
        fixture_utils.init_project_statuses()

    def test_skips(self):
        updated_instance = deepcopy(self.fixture[1])
        updated_instance['Label'] = 'New Data'

        a, updated_count, skipped_count, d = self._sync(updated_instance)
        self.assertEqual(updated_count, 1)
        self.assertEqual(skipped_count, 0)

        a, updated_count, skipped_count, d = self._sync(updated_instance)
        self.assertEqual(skipped_count, 1)
        self.assertEqual(updated_count, 0)


class TestProjectTypeSynchronizer(PicklistSynchronizerTestMixin, TestCase):
    model_class = models.ProjectTypeTracker
    fixture = fixtures.API_PROJECT_TYPE_LIST
    synchronizer = sync.ProjectTypeSynchronizer

    def setUp(self):
        super().setUp()
        fixture_utils.init_project_types()


class TestSourceSynchronizer(PicklistSynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.SourceSynchronizer
    model_class = models.SourceTracker
    fixture = fixtures.API_SOURCE_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_ticket_picklist_call(return_data)


class TestIssueTypeSynchronizer(PicklistSynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.IssueTypeSynchronizer
    model_class = models.IssueTypeTracker
    fixture = fixtures.API_ISSUE_TYPE_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_ticket_picklist_call(return_data)


class TestSubIssueTypeSynchronizer(PicklistSynchronizerRestTestMixin,
                                   TestCase):
    synchronizer_class = sync_rest.SubIssueTypeSynchronizer
    model_class = models.SubIssueTypeTracker
    fixture = fixtures.API_SUB_ISSUE_TYPE_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_ticket_picklist_call(return_data)


class TestTicketTypeSynchronizer(PicklistSynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.TicketTypeSynchronizer
    model_class = models.TicketTypeTracker
    fixture = fixtures.API_TICKET_TYPE_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_ticket_picklist_call(return_data)


class TestDisplayColorSynchronizer(PicklistSynchronizerRestTestMixin,
                                   TestCase):
    synchronizer_class = sync_rest.DisplayColorSynchronizer
    model_class = models.DisplayColorTracker
    fixture = fixtures.API_DISPLAY_COLOR_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_ticket_category_picklist_call(return_data)


class TestServiceCallStatusSynchronizer(PicklistSynchronizerRestTestMixin,
                                        TestCase):
    synchronizer_class = sync_rest.ServiceCallStatusSynchronizer
    model_class = models.ServiceCallStatusTracker
    fixture = fixtures.API_SERVICE_CALL_STATUS_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_service_call_statuses_call(return_data)


class TestTicketCategorySynchronizer(SynchronizerTestMixin, TestCase):
    model_class = models.TicketCategoryTracker
    fixture = fixtures.API_TICKET_CATEGORY_LIST[0]
    update_field = 'Name'

    def setUp(self):
        super().setUp()
        self.synchronizer = sync.TicketCategorySynchronizer()
        fixture_utils.init_display_colors()
        fixture_utils.init_ticket_categories()

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.name, object_data['Name'])
        self.assertEqual(instance.active, object_data['Active'])
        self.assertEqual(instance.display_color.id,
                         object_data['DisplayColorRGB'])

    def test_sync_ticket_category(self):
        """
        Test to ensure ticket category synchronizer saves a Ticket Category
        instance locally.
        """
        self.assertGreater(models.TicketCategory.objects.all().count(), 0)

        instance = models.TicketCategory.objects.get(id=self.fixture['id'])

        self._assert_sync(instance, self.fixture)
        self.assert_sync_job()

    def test_delete_stale_ticket_category(self):
        """
        Test that ticket category is removed if not fetched from the API
        during a full sync.
        """
        ticket_category_qset = models.TicketCategory.objects.all()
        self.assertEqual(ticket_category_qset.count(), 2)

        mocks.api_query_call([])

        synchronizer = sync.TicketCategorySynchronizer(full=True)
        synchronizer.sync()
        self.assertEqual(ticket_category_qset.count(), 0)


class TestResourceSynchronizer(SynchronizerTestMixin, TestCase):
    model_class = models.ResourceTracker
    fixture = fixtures.API_RESOURCE
    update_field = 'LastName'

    def setUp(self):
        super().setUp()
        fixture_utils.init_resources()
        self.synchronizer = sync.ResourceSynchronizer()

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.user_name, object_data['UserName'])
        self.assertEqual(instance.first_name, object_data['FirstName'])
        self.assertEqual(instance.last_name, object_data['LastName'])
        self.assertEqual(instance.email, object_data['Email'])
        self.assertEqual(instance.active, object_data['Active'])

    def test_sync_resource(self):
        """
        Test to ensure resource synchronizer saves a Resource
        instance locally.
        """
        self.assertGreater(models.Resource.objects.all().count(), 0)

        object_data = fixtures.API_RESOURCE
        instance = models.Resource.objects.get(id=object_data['id'])

        self._assert_sync(instance, object_data)
        self.assert_sync_job()

    def test_delete_stale_resources(self):
        """
        Test that  is removed if not fetched from the API during a
        full sync.
        """
        resource_qset = models.Resource.objects.all()
        self.assertEqual(resource_qset.count(), 1)

        mocks.api_query_call([])

        synchronizer = sync.ResourceSynchronizer(full=True)
        synchronizer.sync()
        self.assertEqual(resource_qset.count(), 0)


class TestTicketSecondaryResourceSynchronizer(SynchronizerTestMixin, TestCase):
    model_class = models.TicketSecondaryResourceTracker
    fixture = fixtures.API_SECONDARY_RESOURCE_LIST[0]

    def setUp(self):
        super().setUp()
        self.synchronizer = sync.TicketSecondaryResourceSynchronizer()
        fixture_utils.init_resources()
        fixture_utils.init_tickets()
        fixture_utils.init_secondary_resources()

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.ticket.id, object_data['TicketID'])
        self.assertEqual(instance.resource.id, object_data['ResourceID'])

    def test_sync_ticket_secondary_resource(self):
        self.assertGreater(
            models.TicketSecondaryResource.objects.all().count(), 0)
        instance = \
            models.TicketSecondaryResource.objects.get(id=self.fixture['id'])

        self._assert_sync(instance, self.fixture)
        self.assert_sync_job()

    def test_delete_ticket_secondary_resource(self):
        secondary_resources_qset = models.TicketSecondaryResource.objects.all()
        self.assertEqual(secondary_resources_qset.count(), 2)

        mocks.api_query_call([])

        synchronizer = sync.TicketSecondaryResourceSynchronizer(full=True)
        synchronizer.sync()
        self.assertEqual(secondary_resources_qset.count(), 0)

    def test_skips(self):
        _, updated_count, skipped_count, _ = self._sync(self.fixture)
        self.assertEqual(skipped_count, 1)
        self.assertEqual(updated_count, 0)


class TestAccountSynchronizer(SynchronizerTestMixin, TestCase):
    model_class = models.AccountTracker
    fixture = fixtures.API_ACCOUNT_LIST[0]
    update_field = "AccountName"

    def setUp(self):
        super().setUp()
        self.synchronizer = sync.AccountSynchronizer()
        fixture_utils.init_accounts()

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.name, object_data['AccountName'])
        self.assertEqual(instance.number, str(object_data['AccountNumber']))
        self.assertEqual(instance.active, object_data['Active'])
        self.assertEqual(instance.last_activity_date,
                         object_data['LastActivityDate'])

    def test_sync_account(self):
        self.assertGreater(models.Account.objects.all().count(), 0)
        object_data = fixtures.API_ACCOUNT_LIST[0]
        instance = models.Account.objects.get(id=object_data['id'])

        self._assert_sync(instance, object_data)
        self.assert_sync_job()

    def test_delete_stale_account(self):
        account_qset = models.Account.objects.all()
        self.assertEqual(account_qset.count(), 1)

        mocks.api_query_call([])

        synchronizer = sync.AccountSynchronizer(full=True)
        synchronizer.sync()
        self.assertEqual(account_qset.count(), 0)


class TestAccountPhysicalLocationSynchronizer(SynchronizerRestTestMixin,
                                              TestCase):
    synchronizer_class = sync_rest.AccountPhysicalLocationSynchronizer
    model_class = models.AccountPhysicalLocationTracker
    fixture = fixtures.API_ACCOUNT_PHYSICAL_LOCATION
    update_field = 'name'

    def setUp(self):
        super().setUp()
        fixture_utils.init_accounts()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_account_physical_locations_call(
            return_data)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.account.id, object_data['companyID'])
        self.assertEqual(instance.name, object_data['name'])
        self.assertEqual(instance.active, object_data['isActive'])
        self.assertEqual(instance.primary, object_data['isPrimary'])


class FilterProjectTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.inactive_status = models.ProjectStatus.objects.create(
            label='New (Inactive)', is_active=False, id=9)
        cls.inactive_project = \
            models.Project.objects.create(name='Inactive Project')
        cls.inactive_project.status = cls.inactive_status
        cls.inactive_project.save()


class TestProjectSynchronizer(FilterProjectTestCase, SynchronizerRestTestMixin,
                              TestCase):
    synchronizer_class = sync_rest.ProjectSynchronizer
    model_class = models.ProjectTracker
    fixture = fixtures.API_PROJECT
    update_field = 'description'

    def setUp(self):
        super().setUp()
        fixture_utils.init_contracts()
        fixture_utils.init_resources()
        fixture_utils.init_accounts()
        fixture_utils.init_departments()
        fixture_utils.init_project_statuses()
        fixture_utils.init_project_types()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_projects_call(return_data)

    def test_sync(self):
        instance_dict = {c['id']: c for c in self.fixture_items}

        for instance in self.model_class.objects.all():
            if instance.status.is_active:
                json_data = instance_dict[instance.id]
                self._assert_fields(instance, json_data)

        self.assert_sync_job()

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.name, object_data['projectName'])
        self.assertEqual(instance.number, object_data['projectNumber'])
        self.assertEqual(instance.description, object_data['description'])
        self.assertEqual(instance.actual_hours, object_data['actualHours'])
        self.assertEqual(instance.completed_date,
                         self._parse_datetime(
                             object_data['completedDateTime']).date())
        self.assertEqual(instance.completed_percentage,
                         object_data['completedPercentage'])
        self.assertEqual(instance.duration, object_data['duration'])
        self.assertEqual(instance.start_date,
                         self._parse_datetime(
                             object_data['startDateTime']).date())
        self.assertEqual(instance.end_date,
                         self._parse_datetime(
                             object_data['endDateTime']).date())
        self.assertEqual(instance.estimated_time, object_data['estimatedTime'])
        self.assertEqual(instance.last_activity_date_time,
                         self._parse_datetime(
                             object_data['lastActivityDateTime']))
        self.assertEqual(instance.project_lead_resource.id,
                         object_data['projectLeadResourceID'])
        self.assertEqual(instance.account.id, object_data['companyID'])
        self.assertEqual(instance.status.id, object_data['status'])
        self.assertEqual(instance.type.id, object_data['projectType'])
        self.assertEqual(instance.contract.id, object_data['contractID'])
        self.assertEqual(instance.department.id, object_data['department'])

    def test_sync_filters_projects_in_inactive_status(self):
        """
        Test to ensure that sync does not persist projects in an
        inactive project status.
        """
        project_in_active_status = fixtures.API_PROJECT
        project_fixture = deepcopy(project_in_active_status)
        project_fixture["items"][0]['id'] = '5'
        project_fixture["items"][0]['status'] = self.inactive_status.id

        project_instance = fixture_utils.generate_api_objects(
            [project_fixture, fixtures.API_PROJECT]
        )
        _, patch = mocks.service_api_get_projects_call(project_instance)
        synchronizer = sync_rest.ProjectSynchronizer(full=True)
        synchronizer.sync()

        synced_project_ids = \
            models.Project.objects.values_list('id', flat=True)
        self.assertGreater(models.Project.objects.all().count(), 0)
        self.assertNotIn(project_fixture["items"][0]['id'], synced_project_ids)
        self.assertIn(project_in_active_status["items"][0]['id'],
                      synced_project_ids)
        patch.stop()

    def test_sync_filters_projects_in_complete_status(self):
        """
        Test to ensure that sync does not persist projects in an
        inactive project status.
        """
        project_in_complete_status = fixtures.API_PROJECT
        project_fixture = deepcopy(project_in_complete_status)
        project_fixture["items"][0]['id'] = '6'
        # 5 Is the Autotask system complete status
        project_fixture["items"][0]['status'] = 5

        project_instance = fixture_utils.generate_api_objects(
            [project_fixture, fixtures.API_PROJECT]
        )
        _, patch = mocks.service_api_get_projects_call(project_instance)
        synchronizer = sync_rest.ProjectSynchronizer(full=True)
        synchronizer.sync()

        synced_project_ids = \
            models.Project.objects.values_list('id', flat=True)
        self.assertGreater(models.Project.objects.all().count(), 0)
        self.assertNotIn(project_fixture["items"][0]['id'], synced_project_ids)
        self.assertIn(project_in_complete_status["items"][0]['id'],
                      synced_project_ids)
        patch.stop()


class TestTaskSynchronizer(SynchronizerRestTestMixin,
                           TestAssignNullRelationMixin,
                           FilterProjectTestCase):
    synchronizer_class = sync_rest.TaskSynchronizer
    model_class = models.TaskTracker
    fixture = fixtures.API_TASK
    update_field = "title"
    assign_null_relation_field = 'assignedResourceID'

    def setUp(self):
        super().setUp()
        fixture_utils.init_resources()
        fixture_utils.init_statuses()
        fixture_utils.init_priorities()
        fixture_utils.init_project_statuses()
        fixture_utils.init_projects()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_tasks_call(return_data)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.title, object_data['title'])
        self.assertEqual(instance.number, object_data['taskNumber'])
        self.assertEqual(instance.completed_date,
                         self._parse_datetime(
                             object_data['completedDateTime']))
        self.assertEqual(instance.create_date,
                         self._parse_datetime(object_data['createDateTime']))
        self.assertEqual(instance.start_date,
                         self._parse_datetime(object_data['startDateTime']))
        self.assertEqual(instance.description, object_data['description'])
        self.assertEqual(instance.remaining_hours,
                         object_data['remainingHours'])
        self.assertEqual(instance.estimated_hours,
                         object_data['estimatedHours'])
        self.assertEqual(instance.last_activity_date,
                         self._parse_datetime(
                             object_data['lastActivityDateTime']))

        self.assertEqual(instance.status.id, object_data['status'])
        self.assertEqual(instance.priority.id, object_data['priorityLabel'])
        self.assertEqual(instance.project.id, object_data['projectID'])
        self.assertEqual(instance.assigned_resource.id,
                         object_data['assignedResourceID'])

    def test_sync_filters_tasks_on_inactive_project(self):

        # Add copied task to project in 'Complete' status to ensure it is
        # filtered out during the sync.
        task_fixture = deepcopy(fixtures.API_TASK)
        task_fixture["items"][0]['id'] = '7740'
        task_fixture["items"][0]['projectID'] = self.inactive_project.id

        task_instance = fixture_utils.generate_api_objects(
            [task_fixture, fixtures.API_TASK]
        )
        _, patch = mocks.service_api_get_tasks_call(task_instance)

        synchronizer = sync_rest.TaskSynchronizer(full=True)
        synchronizer.sync()

        synced_task_ids = models.Task.objects.values_list('id', flat=True)
        self.assertGreater(models.Task.objects.all().count(), 0)
        self.assertNotIn(task_fixture["items"][0]['id'], synced_task_ids)
        self.assertIn(fixtures.API_TASK["items"][0]['id'], synced_task_ids)
        patch.stop()

    def test_sync_filters_tasks_on_complete_project(self):
        """
        Test to ensure that sync does not persist tasks on a complete project.
        """
        project = models.Project.objects.create(name='Complete Project')
        project.status = models.ProjectStatus.objects.get(id=5)
        project.save()

        task_fixture = deepcopy(fixtures.API_TASK)
        task_fixture["items"][0]['id'] = '7741'
        task_fixture["items"][0]['projectID'] = project.id

        task_instance = fixture_utils.generate_api_objects(
            [task_fixture, fixtures.API_TASK]
        )
        _, patch = mocks.service_api_get_tasks_call(task_instance)

        synchronizer = sync_rest.TaskSynchronizer(full=True)
        synchronizer.sync()

        synced_task_ids = models.Task.objects.values_list('id', flat=True)
        self.assertGreater(models.Task.objects.all().count(), 0)
        self.assertNotIn(task_fixture["items"][0]['id'], synced_task_ids)
        self.assertIn(fixtures.API_TASK["items"][0]['id'], synced_task_ids)
        patch.stop()


class TestLicenseTypeSynchronizer(PicklistSynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.LicenseTypeSynchronizer
    model_class = models.LicenseTypeTracker
    fixture = fixtures.API_LICENSE_TYPE_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_license_types_call(return_data)


class TestUseTypeSynchronizer(PicklistSynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.UseTypeSynchronizer
    model_class = models.UseTypeTracker
    fixture = fixtures.API_USE_TYPE_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_use_types_call(return_data)


class TestTaskTypeLinkSynchronizer(PicklistSynchronizerRestTestMixin,
                                   TestCase):
    synchronizer_class = sync_rest.TaskTypeLinkSynchronizer
    model_class = models.TaskTypeLinkTracker
    fixture = fixtures.API_TASK_TYPE_LINK_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_task_type_links_call(return_data)


class TestAccountTypeSynchronizer(PicklistSynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.AccountTypeSynchronizer
    model_class = models.AccountTypeTracker
    fixture = fixtures.API_ACCOUNT_TYPE_FIELD

    def _call_api(self, return_data):
        return mocks.service_api_get_account_types_call(return_data)


class TestTaskSecondaryResourceSynchronizer(SynchronizerTestMixin, TestCase):
    model_class = models.TaskSecondaryResourceTracker
    fixture = fixtures.API_TASK_SECONDARY_RESOURCE

    def setUp(self):
        super().setUp()
        self.synchronizer = sync.TaskSecondaryResourceSynchronizer()
        fixture_utils.init_resources()
        fixture_utils.init_projects()
        fixture_utils.init_tasks()
        fixture_utils.init_task_secondary_resources()

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.resource.id, object_data['ResourceID'])
        self.assertEqual(instance.task.id, object_data['TaskID'])

    def test_sync_task_secondary_resource(self):
        self.assertGreater(
            models.TaskSecondaryResource.objects.all().count(), 0)
        instance = \
            models.TaskSecondaryResource.objects.get(id=self.fixture['id'])

        self._assert_sync(instance, self.fixture)
        self.assert_sync_job()

    def test_delete_task_secondary_resource(self):
        secondary_resources_qset = models.TaskSecondaryResource.objects.all()
        self.assertEqual(secondary_resources_qset.count(), 1)

        mocks.api_query_call([])

        synchronizer = sync.TaskSecondaryResourceSynchronizer(full=True)
        synchronizer.sync()
        self.assertEqual(secondary_resources_qset.count(), 0)

    def test_skips(self):
        _, updated_count, skipped_count, _ = self._sync(self.fixture)
        self.assertEqual(skipped_count, 1)
        self.assertEqual(updated_count, 0)


class TestPhaseSynchronizer(SynchronizerTestMixin, TestCase):
    model_class = models.PhaseTracker
    fixture = fixtures.API_PHASE
    update_field = "Title"

    def setUp(self):
        super().setUp()
        mocks.init_api_connection(Wrapper)
        self.synchronizer = sync.PhaseSynchronizer()

        fixture_utils.init_projects()
        fixture_utils.init_phases()
        fixture_utils.init_tasks()

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.title, object_data['Title'])
        self.assertEqual(instance.start_date, object_data['StartDate'])
        self.assertEqual(instance.description, object_data['Description'])
        self.assertEqual(instance.estimated_hours,
                         object_data['EstimatedHours'])
        self.assertEqual(instance.last_activity_date,
                         object_data['LastActivityDateTime'])
        self.assertEqual(instance.number, object_data['PhaseNumber'])

    def test_sync_phase(self):
        """
        Test to ensure task synchronizer saves a Phase instance locally.
        """
        self.assertGreater(models.Phase.objects.all().count(), 0)

        instance = models.Phase.objects.get(id=self.fixture['id'])

        self._assert_sync(instance, self.fixture)
        self.assert_sync_job()

    def test_delete_stale_phases(self):
        """
        Local task should be deleted if not returned during a full sync
        """
        qset = models.Phase.objects.all()
        self.assertEqual(qset.count(), 1)

        mocks.api_query_call([])

        synchronizer = sync.PhaseSynchronizer(full=True)
        synchronizer.sync()
        self.assertEqual(qset.count(), 0)


class TestTimeEntrySynchronizer(SynchronizerTestMixin, TestCase):
    model_class = models.TimeEntryTracker
    fixture = fixtures.API_TIME_ENTRY_TICKET

    def setUp(self):
        super().setUp()
        self.synchronizer = sync.TimeEntrySynchronizer()

        mocks.init_api_connection(Wrapper)
        mocks.init_api_rest_connection()

        fixture_utils.init_resources()
        fixture_utils.init_tickets()
        fixture_utils.init_tasks()

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.date_worked, object_data['DateWorked'])
        self.assertEqual(instance.start_date_time,
                         object_data['StartDateTime'])
        self.assertEqual(instance.end_date_time, object_data['EndDateTime'])
        self.assertEqual(instance.summary_notes, object_data['SummaryNotes'])
        self.assertEqual(instance.internal_notes, object_data['InternalNotes'])
        self.assertEqual(instance.non_billable, object_data['NonBillable'])
        self.assertEqual(instance.hours_worked, object_data['HoursWorked'])
        self.assertEqual(instance.hours_to_bill, object_data['HoursToBill'])
        self.assertEqual(instance.offset_hours, object_data['OffsetHours'])
        self.assertEqual(instance.ticket.id, object_data['TicketID'])
        self.assertEqual(instance.resource.id, object_data['ResourceID'])

    def test_sync_time_entry(self):
        """
        Test to ensure synchronizer saves a time entry instance locally.
        """
        time_entries = fixture_utils.generate_objects(
            'TimeEntry', fixtures.API_TIME_ENTRY_LIST)
        mocks.api_query_call(time_entries)
        synchronizer = sync.TimeEntrySynchronizer()
        synchronizer.sync()

        self.assertGreater(models.TimeEntry.objects.all().count(), 0)

        instance = models.TimeEntry.objects.get(id=self.fixture['id'])

        ticket = models.Ticket.objects.first()
        ticket.id = self.fixture['TicketID']
        instance.ticket = ticket

        resource = models.Resource.objects.first()
        resource.id = self.fixture['ResourceID']
        instance.resource = resource

        self._assert_sync(instance, self.fixture)
        self.assert_sync_job()

    def test_sync_time_entry_dropped(self):
        """
        Verify that a time entry does not get saved locally if its ticket
        does not already exist in the local database.
        """
        time_entry_count = models.TimeEntry.objects.all().count()

        synchronizer = sync.TimeEntrySynchronizer(full=True)
        synchronizer.sync()
        sync_job = models.SyncJob.objects.last()

        # Time entry for time entry ticket is not saved locally
        # and is subsequently removed.
        self.assertEqual(models.TimeEntry.objects.all().count(), 0)
        self.assertEqual(sync_job.added, 0)
        self.assertEqual(sync_job.updated, 0)
        self.assertEqual(sync_job.deleted, time_entry_count)

    def test_delete_stale_time_entries(self):
        """
        Verify that time entry is deleted if not returned during a full sync
        """
        time_entries = fixture_utils.generate_objects(
            'TimeEntry', fixtures.API_TIME_ENTRY_LIST)
        mocks.api_query_call(time_entries)
        synchronizer = sync.TimeEntrySynchronizer()
        synchronizer.sync()

        qset = models.TimeEntry.objects.all()
        self.assertEqual(qset.count(), len(fixtures.API_TIME_ENTRY_LIST))

        mocks.api_query_call([])

        synchronizer = sync.TimeEntrySynchronizer(full=True)
        synchronizer.sync()

        qset = models.TimeEntry.objects.all()
        self.assertEqual(qset.count(), 0)

    def test_batch_queries_creates_multiple_batches(self):
        """
        Verify that build batch query method returns multiple batches
        ticket and task queries.
        """
        max_id_limit = 500
        settings = DjautotaskSettings().get_settings()
        batch_size = settings.get('batch_query_size')

        synchronizer = sync.TimeEntrySynchronizer()
        sync_job = models.SyncJob.objects.filter(entity_name='TimeEntry')

        # Simulate ticket IDs
        object_ids = random.sample(range(1, max_id_limit), batch_size + 50)
        _, _patch = mocks.create_mock_call(
            'django.db.models.query.QuerySet.values_list', object_ids
        )

        batch_query_list = synchronizer.build_batch_queries(sync_job)

        # With a max batch size of 400, a set of 450 object IDs should result
        # in 4 Query objects being returned in the list. (2 for tickets, 2 for
        # tasks)
        self.assertEqual(len(batch_query_list), 4)

        _patch.stop()

    def test_batch_queries_returns_query_list(self):
        """
        Verify that an empty list is returned when no tickets or
        tasks are present in the database.
        """
        _, _patch = mocks.create_mock_call(
            'django.db.models.query.QuerySet.values_list', []
        )
        synchronizer = sync.TimeEntrySynchronizer()
        sync_job = models.SyncJob.objects.filter(entity_name='TimeEntry')

        batch_query_list = synchronizer.build_batch_queries(sync_job)

        self.assertEqual(len(batch_query_list), 0)

        _patch.stop()

    def test_skips(self):
        self._sync(self.fixture)

        updated_instance = deepcopy(self.fixture)
        updated_instance["HoursWorked"] = 3.000

        _, updated_count, skipped_count, _ = self._sync(updated_instance)
        self.assertEqual(updated_count, 1)
        self.assertEqual(skipped_count, 0)

        _, updated_count, skipped_count, _ = self._sync(updated_instance)
        self.assertEqual(skipped_count, 1)
        self.assertEqual(updated_count, 0)


class TestAllocationCodeSynchronizer(SynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.AllocationCodeSynchronizer
    model_class = models.AllocationCodeTracker
    fixture = fixtures.API_ALLOCATION_CODE
    update_field = 'name'

    def setUp(self):
        super().setUp()
        fixture_utils.init_use_types()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_allocation_codes_call(return_data)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.name, object_data.get('name'))
        self.assertEqual(instance.description, object_data.get('description'))
        self.assertEqual(instance.active, object_data.get('isActive'))
        self.assertEqual(instance.use_type.id, object_data.get('useType'))


class TestRoleSynchronizer(SynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.RoleSynchronizer
    model_class = models.RoleTracker
    fixture = fixtures.API_ROLE
    update_field = 'description'

    def setUp(self):
        super().setUp()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_roles_call(return_data)

    def _assert_fields(self, instance, json_data):
        self.assertEqual(instance.id, json_data['id'])
        self.assertEqual(instance.name, json_data['name'])
        self.assertEqual(instance.description, json_data['description'])
        self.assertEqual(instance.active, json_data['isActive'])
        self.assertEqual(instance.hourly_factor, json_data['hourlyFactor'])
        self.assertEqual(instance.hourly_rate, json_data['hourlyRate'])
        self.assertEqual(instance.role_type, json_data['roleType'])
        self.assertEqual(instance.system_role, json_data['isSystemRole'])


class TestDepartmentSynchronizer(SynchronizerRestTestMixin,
                                 TestCase):
    synchronizer_class = sync_rest.DepartmentSynchronizer
    model_class = models.DepartmentTracker
    fixture = fixtures.API_DEPARTMENT
    update_field = 'description'

    def setUp(self):
        super().setUp()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_departments_call(return_data)

    def _assert_fields(self, instance, json_data):
        self.assertEqual(instance.id, json_data['id'])
        self.assertEqual(instance.name, json_data['name'])
        self.assertEqual(instance.description, json_data['description'])
        self.assertEqual(instance.number, json_data['number'])


class TestResourceRoleDepartmentSynchronizer(SynchronizerRestTestMixin,
                                             TestCase):
    synchronizer_class = sync_rest.ResourceRoleDepartmentSynchronizer
    model_class = models.ResourceRoleDepartmentTracker
    fixture = fixtures.API_RESOURCE_ROLE_DEPARTMENT
    update_field = 'active'

    def setUp(self):
        super().setUp()
        fixture_utils.init_departments()
        fixture_utils.init_roles()
        fixture_utils.init_resources()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_resource_role_departments_call(
            return_data)

    def _assert_fields(self, instance, json_data):
        self.assertEqual(instance.id, json_data['id'])
        self.assertEqual(instance.active, json_data['isActive'])
        self.assertEqual(instance.default, json_data['isDefault'])
        self.assertEqual(instance.resource.id, json_data['resourceID'])
        self.assertEqual(instance.role.id, json_data['roleID'])
        self.assertEqual(instance.department.id, json_data['departmentID'])
        self.assertEqual(instance.department_lead,
                         json_data['isDepartmentLead'])


class TestResourceServiceDeskRoleSynchronizer(SynchronizerRestTestMixin,
                                              TestCase):
    synchronizer_class = sync_rest.ResourceServiceDeskRoleSynchronizer
    model_class = models.ResourceServiceDeskRoleTracker
    fixture = fixtures.API_RESOURCE_SERVICE_DESK_ROLE
    update_field = 'active'

    def setUp(self):
        super().setUp()
        fixture_utils.init_roles()
        fixture_utils.init_resources()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_resource_service_desk_roles_call(
            return_data)

    def _assert_fields(self, instance, json_data):
        self.assertEqual(instance.id, json_data['id'])
        self.assertEqual(instance.active, json_data['isActive'])
        self.assertEqual(instance.default, json_data['isDefault'])
        self.assertEqual(instance.resource.id, json_data['resourceID'])
        self.assertEqual(instance.role.id, json_data['roleID'])


class TestContractSynchronizer(SynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.ContractSynchronizer
    model_class = models.ContractTracker
    fixture = fixtures.API_CONTRACT
    update_field = 'name'

    def setUp(self):
        super().setUp()
        fixture_utils.init_accounts()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_contracts_call(return_data)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.name, object_data['contractName'])
        self.assertEqual(instance.number, object_data['contractNumber'])
        self.assertEqual(instance.status, str(object_data['status']))
        self.assertEqual(instance.account.id, object_data['companyID'])


class TestServiceCallSynchronizer(SynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.ServiceCallSynchronizer
    model_class = models.ServiceCallTracker
    fixture = fixtures.API_SERVICE_CALL
    update_field = 'description'

    def setUp(self):
        super().setUp()
        fixture_utils.init_service_call_statuses()
        fixture_utils.init_resources()
        fixture_utils.init_account_types()
        fixture_utils.init_accounts()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_service_calls_call(return_data)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.description, object_data['description'])
        self.assertEqual(instance.duration, object_data['duration'])
        self.assertEqual(instance.complete, object_data['isComplete'])
        self.assertEqual(
            instance.create_date_time,
            self._parse_datetime(object_data['createDateTime'])
        )
        self.assertEqual(
            instance.start_date_time,
            self._parse_datetime(object_data['startDateTime'])
        )
        self.assertEqual(
            instance.end_date_time,
            self._parse_datetime(object_data['endDateTime'])
        )
        self.assertEqual(
            instance.canceled_date_time,
            self._parse_datetime(object_data['canceledDateTime'])
        )
        self.assertEqual(
            instance.last_modified_date_time,
            self._parse_datetime(object_data['lastModifiedDateTime'])
        )
        self.assertEqual(instance.status.id, object_data['status'])
        self.assertEqual(instance.account.id, object_data['companyID'])
        self.assertEqual(
            instance.creator_resource.id, object_data['creatorResourceID'])
        self.assertEqual(
            instance.canceled_by_resource.id,
            object_data['canceledByResourceID']
        )


class TestServiceCallTicketSynchronizer(SynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.ServiceCallTicketSynchronizer
    model_class = models.ServiceCallTicketTracker
    fixture = fixtures.API_SERVICE_CALL_TICKET
    update_field = 'ticket_id'

    def setUp(self):
        super().setUp()
        fixture_utils.init_tickets()
        fixture_utils.init_service_call_statuses()
        fixture_utils.init_accounts()
        fixture_utils.init_service_calls()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_service_call_tickets_call(return_data)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.service_call.id,
                         object_data['serviceCallID'])
        self.assertEqual(instance.ticket.id, object_data['ticketID'])

    def test_sync_update(self):
        ticket = models.Ticket.objects.first()
        extra_ticket = deepcopy(ticket)
        extra_ticket.id = extra_ticket.id + 1
        extra_ticket.save()
        super().test_sync_update()


class TestServiceCallTaskSynchronizer(SynchronizerRestTestMixin, TestCase):
    synchronizer_class = sync_rest.ServiceCallTaskSynchronizer
    model_class = models.ServiceCallTaskTracker
    fixture = fixtures.API_SERVICE_CALL_TASK
    update_field = 'task_id'

    def setUp(self):
        super().setUp()
        fixture_utils.init_projects()
        fixture_utils.init_tasks()
        fixture_utils.init_service_call_statuses()
        fixture_utils.init_accounts()
        fixture_utils.init_service_calls()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_service_call_tasks_call(return_data)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.service_call.id,
                         object_data['serviceCallID'])
        self.assertEqual(instance.task.id, object_data['taskID'])

    def test_sync_update(self):
        task = models.Task.objects.first()
        extra_task = deepcopy(task)
        extra_task.id = extra_task.id + 1
        extra_task.save()
        super().test_sync_update()


class TestServiceCallTicketResourceSynchronizer(SynchronizerRestTestMixin,
                                                TestCase):
    synchronizer_class = sync_rest.ServiceCallTicketResourceSynchronizer
    model_class = models.ServiceCallTicketResourceTracker
    fixture = fixtures.API_SERVICE_CALL_TICKET_RESOURCE
    update_field = 'resource_id'

    def setUp(self):
        super().setUp()
        fixture_utils.init_tickets()
        fixture_utils.init_resources()
        fixture_utils.init_service_call_tickets()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_service_call_ticket_resources_call(
            return_data)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.service_call_ticket.id,
                         object_data['serviceCallTicketID'])
        self.assertEqual(instance.resource.id, object_data['resourceID'])


class TestServiceCallTaskResourceSynchronizer(SynchronizerRestTestMixin,
                                              TestCase):
    synchronizer_class = sync_rest.ServiceCallTaskResourceSynchronizer
    model_class = models.ServiceCallTaskResourceTracker
    fixture = fixtures.API_SERVICE_CALL_TASK_RESOURCE
    update_field = 'resource_id'

    def setUp(self):
        super().setUp()
        fixture_utils.init_projects()
        fixture_utils.init_tasks()
        fixture_utils.init_resources()
        fixture_utils.init_service_call_tasks()
        self._sync(self.fixture)

    def _call_api(self, return_data):
        return mocks.service_api_get_service_call_task_resources_call(
            return_data)

    def _assert_fields(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.service_call_task.id,
                         object_data['serviceCallTaskID'])
        self.assertEqual(instance.resource.id, object_data['resourceID'])


class TestTaskPredecessorSynchronizer(SynchronizerTestMixin, TestCase):
    model_class = models.TaskPredecessorTracker
    fixture = fixtures.API_TASK_PREDECESSOR
    update_field = 'LagDays'
    updated_data = 2

    def setUp(self):
        super().setUp()
        self.synchronizer = sync.TaskPredecessorSynchronizer()

        mocks.init_api_connection(Wrapper)
        fixture_utils.init_projects()
        fixture_utils.init_tasks()

        project = models.Project.objects.first()
        models.Task.objects.create(
            id=fixtures.API_TASK_PREDECESSOR['SuccessorTaskID'],
            title='Successor Task', project=project)
        fixture_utils.init_task_predecessors()

    def _assert_sync(self, instance, object_data):
        self.assertEqual(instance.id, object_data['id'])
        self.assertEqual(instance.lag_days, object_data['LagDays'])
        self.assertEqual(instance.predecessor_task.id,
                         object_data['PredecessorTaskID'])
        self.assertEqual(instance.successor_task.id,
                         object_data['SuccessorTaskID'])

    def test_sync_task_predecessor(self):
        self.assertGreater(models.TaskPredecessor.objects.count(), 0)

        object_data = fixtures.API_TASK_PREDECESSOR
        instance = models.TaskPredecessor.objects.get(id=object_data['id'])

        self._assert_sync(instance, object_data)
        self.assert_sync_job()

    def test_batch_queries_creates_multiple_batches(self):
        """
        Verify that the build batch query method returns multiple batches
        of task predecessor queries.
        """
        max_id_limit = 500
        settings = DjautotaskSettings().get_settings()
        batch_size = settings.get('batch_query_size')

        synchronizer = sync.TaskPredecessorSynchronizer()
        sync_job = models.SyncJob.objects.filter(entity_name='TaskPredecessor')

        # Create some fake task IDs
        task_ids = random.sample(range(1, max_id_limit), batch_size + 50)
        _, _patch = mocks.create_mock_call(
            'django.db.models.query.QuerySet.values_list', task_ids
        )

        batch_query_list = synchronizer.build_batch_queries(sync_job)

        # With a batch size of 400 and 450 task IDs in the database, a list
        # of 3 Query objects should be returned with each object
        # having a maximum of approximately 400 conditions.
        self.assertEqual(len(batch_query_list), 3)
        for query in batch_query_list:
            # Count number of condition tags in the XML.
            # Since each condition has 2 condition tags, divide by 2.
            condition_count = int(query.get_query_xml().count('condition') / 2)
            self.assertLessEqual(condition_count, batch_size + 1)
        _patch.stop()
