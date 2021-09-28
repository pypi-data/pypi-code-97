# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import packaging.version
import pkg_resources

import google.auth  # type: ignore
import google.api_core  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.deploy_v1.types import cloud_deploy
from google.longrunning import operations_pb2  # type: ignore

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-deploy",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()

try:
    # google.auth.__version__ was added in 1.26.0
    _GOOGLE_AUTH_VERSION = google.auth.__version__
except AttributeError:
    try:  # try pkg_resources if it is available
        _GOOGLE_AUTH_VERSION = pkg_resources.get_distribution("google-auth").version
    except pkg_resources.DistributionNotFound:  # pragma: NO COVER
        _GOOGLE_AUTH_VERSION = None


class CloudDeployTransport(abc.ABC):
    """Abstract transport class for CloudDeploy."""

    AUTH_SCOPES = ("https://www.googleapis.com/auth/cloud-platform",)

    DEFAULT_HOST: str = "clouddeploy.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
        **kwargs,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        scopes_kwargs = self._get_scopes_kwargs(self._host, scopes)

        # Save the scopes.
        self._scopes = scopes

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )

        # If the credentials are service account credentials, then always try to use self signed JWT.
        if (
            always_use_jwt_access
            and isinstance(credentials, service_account.Credentials)
            and hasattr(service_account.Credentials, "with_always_use_jwt_access")
        ):
            credentials = credentials.with_always_use_jwt_access(True)

        # Save the credentials.
        self._credentials = credentials

    # TODO(busunkim): This method is in the base transport
    # to avoid duplicating code across the transport classes. These functions
    # should be deleted once the minimum required versions of google-auth is increased.

    # TODO: Remove this function once google-auth >= 1.25.0 is required
    @classmethod
    def _get_scopes_kwargs(
        cls, host: str, scopes: Optional[Sequence[str]]
    ) -> Dict[str, Optional[Sequence[str]]]:
        """Returns scopes kwargs to pass to google-auth methods depending on the google-auth version"""

        scopes_kwargs = {}

        if _GOOGLE_AUTH_VERSION and (
            packaging.version.parse(_GOOGLE_AUTH_VERSION)
            >= packaging.version.parse("1.25.0")
        ):
            scopes_kwargs = {"scopes": scopes, "default_scopes": cls.AUTH_SCOPES}
        else:
            scopes_kwargs = {"scopes": scopes or cls.AUTH_SCOPES}

        return scopes_kwargs

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.list_delivery_pipelines: gapic_v1.method.wrap_method(
                self.list_delivery_pipelines,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_delivery_pipeline: gapic_v1.method.wrap_method(
                self.get_delivery_pipeline,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_delivery_pipeline: gapic_v1.method.wrap_method(
                self.create_delivery_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.update_delivery_pipeline: gapic_v1.method.wrap_method(
                self.update_delivery_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.delete_delivery_pipeline: gapic_v1.method.wrap_method(
                self.delete_delivery_pipeline,
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.list_targets: gapic_v1.method.wrap_method(
                self.list_targets,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_target: gapic_v1.method.wrap_method(
                self.get_target,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_target: gapic_v1.method.wrap_method(
                self.create_target, default_timeout=60.0, client_info=client_info,
            ),
            self.update_target: gapic_v1.method.wrap_method(
                self.update_target, default_timeout=60.0, client_info=client_info,
            ),
            self.delete_target: gapic_v1.method.wrap_method(
                self.delete_target, default_timeout=60.0, client_info=client_info,
            ),
            self.list_releases: gapic_v1.method.wrap_method(
                self.list_releases,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_release: gapic_v1.method.wrap_method(
                self.get_release,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_release: gapic_v1.method.wrap_method(
                self.create_release, default_timeout=60.0, client_info=client_info,
            ),
            self.approve_rollout: gapic_v1.method.wrap_method(
                self.approve_rollout, default_timeout=60.0, client_info=client_info,
            ),
            self.list_rollouts: gapic_v1.method.wrap_method(
                self.list_rollouts,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.get_rollout: gapic_v1.method.wrap_method(
                self.get_rollout,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
            self.create_rollout: gapic_v1.method.wrap_method(
                self.create_rollout, default_timeout=60.0, client_info=client_info,
            ),
            self.get_config: gapic_v1.method.wrap_method(
                self.get_config,
                default_retry=retries.Retry(
                    initial=1.0,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=60.0,
                ),
                default_timeout=60.0,
                client_info=client_info,
            ),
        }

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Return the client designed to process long-running operations."""
        raise NotImplementedError()

    @property
    def list_delivery_pipelines(
        self,
    ) -> Callable[
        [cloud_deploy.ListDeliveryPipelinesRequest],
        Union[
            cloud_deploy.ListDeliveryPipelinesResponse,
            Awaitable[cloud_deploy.ListDeliveryPipelinesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.GetDeliveryPipelineRequest],
        Union[cloud_deploy.DeliveryPipeline, Awaitable[cloud_deploy.DeliveryPipeline]],
    ]:
        raise NotImplementedError()

    @property
    def create_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.CreateDeliveryPipelineRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateDeliveryPipelineRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_delivery_pipeline(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteDeliveryPipelineRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_targets(
        self,
    ) -> Callable[
        [cloud_deploy.ListTargetsRequest],
        Union[
            cloud_deploy.ListTargetsResponse,
            Awaitable[cloud_deploy.ListTargetsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_target(
        self,
    ) -> Callable[
        [cloud_deploy.GetTargetRequest],
        Union[cloud_deploy.Target, Awaitable[cloud_deploy.Target]],
    ]:
        raise NotImplementedError()

    @property
    def create_target(
        self,
    ) -> Callable[
        [cloud_deploy.CreateTargetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def update_target(
        self,
    ) -> Callable[
        [cloud_deploy.UpdateTargetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def delete_target(
        self,
    ) -> Callable[
        [cloud_deploy.DeleteTargetRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def list_releases(
        self,
    ) -> Callable[
        [cloud_deploy.ListReleasesRequest],
        Union[
            cloud_deploy.ListReleasesResponse,
            Awaitable[cloud_deploy.ListReleasesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_release(
        self,
    ) -> Callable[
        [cloud_deploy.GetReleaseRequest],
        Union[cloud_deploy.Release, Awaitable[cloud_deploy.Release]],
    ]:
        raise NotImplementedError()

    @property
    def create_release(
        self,
    ) -> Callable[
        [cloud_deploy.CreateReleaseRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def approve_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.ApproveRolloutRequest],
        Union[
            cloud_deploy.ApproveRolloutResponse,
            Awaitable[cloud_deploy.ApproveRolloutResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_rollouts(
        self,
    ) -> Callable[
        [cloud_deploy.ListRolloutsRequest],
        Union[
            cloud_deploy.ListRolloutsResponse,
            Awaitable[cloud_deploy.ListRolloutsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def get_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.GetRolloutRequest],
        Union[cloud_deploy.Rollout, Awaitable[cloud_deploy.Rollout]],
    ]:
        raise NotImplementedError()

    @property
    def create_rollout(
        self,
    ) -> Callable[
        [cloud_deploy.CreateRolloutRequest],
        Union[operations_pb2.Operation, Awaitable[operations_pb2.Operation]],
    ]:
        raise NotImplementedError()

    @property
    def get_config(
        self,
    ) -> Callable[
        [cloud_deploy.GetConfigRequest],
        Union[cloud_deploy.Config, Awaitable[cloud_deploy.Config]],
    ]:
        raise NotImplementedError()


__all__ = ("CloudDeployTransport",)
