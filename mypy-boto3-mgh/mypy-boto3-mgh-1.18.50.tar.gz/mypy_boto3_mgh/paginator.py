"""
Type annotations for mgh service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_mgh import MigrationHubClient
    from mypy_boto3_mgh.paginator import (
        ListApplicationStatesPaginator,
        ListCreatedArtifactsPaginator,
        ListDiscoveredResourcesPaginator,
        ListMigrationTasksPaginator,
        ListProgressUpdateStreamsPaginator,
    )

    client: MigrationHubClient = boto3.client("mgh")

    list_application_states_paginator: ListApplicationStatesPaginator = client.get_paginator("list_application_states")
    list_created_artifacts_paginator: ListCreatedArtifactsPaginator = client.get_paginator("list_created_artifacts")
    list_discovered_resources_paginator: ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
    list_migration_tasks_paginator: ListMigrationTasksPaginator = client.get_paginator("list_migration_tasks")
    list_progress_update_streams_paginator: ListProgressUpdateStreamsPaginator = client.get_paginator("list_progress_update_streams")
    ```
"""
from typing import Generic, Iterator, Sequence, TypeVar

from botocore.paginate import PageIterator
from botocore.paginate import Paginator as Boto3Paginator

from .type_defs import (
    ListApplicationStatesResultTypeDef,
    ListCreatedArtifactsResultTypeDef,
    ListDiscoveredResourcesResultTypeDef,
    ListMigrationTasksResultTypeDef,
    ListProgressUpdateStreamsResultTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListApplicationStatesPaginator",
    "ListCreatedArtifactsPaginator",
    "ListDiscoveredResourcesPaginator",
    "ListMigrationTasksPaginator",
    "ListProgressUpdateStreamsPaginator",
)


_ItemTypeDef = TypeVar("_ItemTypeDef")


class _PageIterator(Generic[_ItemTypeDef], PageIterator):
    def __iter__(self) -> Iterator[_ItemTypeDef]:
        """
        Proxy method to specify iterator item type.
        """


class ListApplicationStatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.50/reference/services/mgh.html#MigrationHub.Paginator.ListApplicationStates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listapplicationstatespaginator)
    """

    def paginate(
        self,
        *,
        ApplicationIds: Sequence[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> _PageIterator[ListApplicationStatesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.50/reference/services/mgh.html#MigrationHub.Paginator.ListApplicationStates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listapplicationstatespaginator)
        """


class ListCreatedArtifactsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.50/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listcreatedartifactspaginator)
    """

    def paginate(
        self,
        *,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> _PageIterator[ListCreatedArtifactsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.50/reference/services/mgh.html#MigrationHub.Paginator.ListCreatedArtifacts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listcreatedartifactspaginator)
        """


class ListDiscoveredResourcesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.50/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listdiscoveredresourcespaginator)
    """

    def paginate(
        self,
        *,
        ProgressUpdateStream: str,
        MigrationTaskName: str,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> _PageIterator[ListDiscoveredResourcesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.50/reference/services/mgh.html#MigrationHub.Paginator.ListDiscoveredResources.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listdiscoveredresourcespaginator)
        """


class ListMigrationTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.50/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listmigrationtaskspaginator)
    """

    def paginate(
        self, *, ResourceName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> _PageIterator[ListMigrationTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.50/reference/services/mgh.html#MigrationHub.Paginator.ListMigrationTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listmigrationtaskspaginator)
        """


class ListProgressUpdateStreamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.50/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listprogressupdatestreamspaginator)
    """

    def paginate(
        self, *, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> _PageIterator[ListProgressUpdateStreamsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.18.50/reference/services/mgh.html#MigrationHub.Paginator.ListProgressUpdateStreams.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_mgh/paginators.html#listprogressupdatestreamspaginator)
        """
