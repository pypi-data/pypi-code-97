from schema import Optional, Schema, Or
from typing import List, Union, TYPE_CHECKING

from configcrunch import YamlConfigDocument, DocReference, ConfigcrunchError, REMOVE
from configcrunch import load_subdocument
from configcrunch.abstract import variable_helper
from riptide.config.document.command import Command
from riptide.config.document.service import Service

if TYPE_CHECKING:
    from riptide.config.document.project import Project

HEADER = 'app'


class App(YamlConfigDocument):
    """
    An application.

    Consists of (multiple) :class:`riptide.config.document.service.Service`
    and (multiple) :class:`riptide.config.document.command.Command`
    and is usually included in a :class:`riptide.config.document.project.Project`.
    """
    @classmethod
    def header(cls) -> str:
        return HEADER

    @classmethod
    def schema(cls) -> Schema:
        """
        name: str
            Name describing this app.

        [notices]
            [usage]: str
                Text that will be shown when the interactive `setup wizard </user_docs/4_project.html>`_ ist started.

                This text should describe additional steps needed to finish the setup of the app and general
                usage notes.

            [installation]: str
                Text that will be shown, when the user selects a new installation (from scratch) for this app.

                This text should explain how to execute the first-time-setup of this app when using Riptide.

        [import]
            {key}
                Files and directories to import during the interactive setup wizard.

                target: str
                    Target path that the file or directory should be imported to,
                    relative to the directory of the riptide.yml

                name: str
                    Human-readable name of this import file. This is displayed during the interactive setup and should
                    explain what kind of file or directory is imported.

        [services]
            {key}: :class:`~riptide.config.document.service.Service`
                Services for this app.

        [commands]
            {key}: :class:`~riptide.config.document.command.Command`
                Commands for this app.

        [unimportant_paths]: List[str]
            Normally all files inside containers are shared with the host (for commands and services with role 'src').
            This list specifies files that don't need to be synced with the host. This means, that these files
            will only be uploaded to the container on start and changes will not be visible on the host. Changes that
            are made on the host file system may also not be visible inside the container. This increases performance
            on non-native platforms (Mac and Windows).

            This feature is only enabled if the system configuration performance setting ``dont_sync_unimportant_src``
            is enabled. If the feature is disabled, all files are shared with the host. See the documentation for that
            setting for more information.

            All paths are relative to the src of the project. Only directories are supported.


        **Example Document:**

        .. code-block:: yaml

            app:
              name: example
              notices:
                usage: Hello World!
              import:
                example:
                  target: path/inside/project
                  name: Example Files
              services:
                example:
                  $ref: /service/example
              commands:
                example:
                  $ref: /command/example
        """
        return Schema(
            {
                Optional('$ref'): str,  # reference to other App documents
                'name': str,
                Optional('notices'): {
                    Optional('usage'): str,
                    Optional('installation'): str
                },
                Optional('import'): {
                    str: {
                        'target': str,
                        'name': str
                    }
                },
                Optional('services'): {
                    str: DocReference(Service)
                },
                Optional('commands'): {
                    str: DocReference(Command)
                },
                Optional('unimportant_paths'): [str]
            }
        )

    def validate(self):
        """
        Initialise the optional services and command dicts.
        Has to be done after validate because of some issues with Schema validation error handling :(
        """
        ret_val = super().validate()
        if ret_val:
            if "services" not in self:
                self.doc["services"] = {}

            if "commands" not in self:
                self.doc["commands"] = {}
        return ret_val

    def _load_subdocuments(self, lookup_paths: List[str]):
        if "services" in self and self["services"] != REMOVE:
            for key, servicedoc in self["services"].items():
                if servicedoc != REMOVE:
                    self["services"][key] = load_subdocument(servicedoc, self, Service, lookup_paths)
                    if not isinstance(self["services"][key].doc, dict):
                        raise ConfigcrunchError(
                            f"Error loading Service for App: The service with the name {key} needs to be an object in the source document."
                        )
                    self["services"][key]["$name"] = key

        if "commands" in self and self["commands"] != REMOVE:
            for key, commanddoc in self["commands"].items():
                if commanddoc != REMOVE:
                    self["commands"][key] = load_subdocument(commanddoc, self, Command, lookup_paths)
                    if not isinstance(self["commands"][key].doc, dict):
                        raise ConfigcrunchError(
                            f"Error loading Command for App: The command with the name {key} needs to be an object in the source document."
                        )
                    self["commands"][key]["$name"] = key

        return self

    def error_str(self) -> str:
        return f"{self.__class__.__name__}<{(self['name'] if 'name' in self else '???')}>"

    @variable_helper
    def parent(self) -> 'Project':
        """
        Returns the project that this app belongs to.

        Example usage::

            something: '{{ parent().src }}'

        Example result::

            something: '.'
        """
        # noinspection PyTypeChecker
        return super().parent()

    @variable_helper
    def get_service_by_role(self, role_name: str) -> Union[Service, None]:
        """
        Returns any service with the given role name (first found) or None.

        Example usage::

            something: '{{ get_service_by_role("main")["$name"] }}'

        Example result::

            something: 'service1'

        :param role_name: Role to search for
        """
        for service in self["services"].values():
            if "roles" in service and role_name in service["roles"]:
                return service
        raise ValueError(f"No service with role {role_name} found in the app.")

    @variable_helper
    def get_services_by_role(self, role_name: str) -> List[Service]:
        """
        Returns all services with the given role name.

        :param role_name: Role to search for
        """
        services = []
        for service in self["services"].values():
            if "roles" in service and role_name in service["roles"]:
                services.append(service)
        return services
