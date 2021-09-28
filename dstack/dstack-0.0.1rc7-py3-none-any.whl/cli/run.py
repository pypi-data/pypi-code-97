import json
import os
import sys
from argparse import Namespace

import requests
import yaml
from git import InvalidGitRepositoryError
from jsonschema import validate, ValidationError

from dstack.cli.schema import workflows_schema_yaml
from dstack.cli.common import load_workflows, load_variables, load_repo_data
from dstack.config import get_config, ConfigurationError


def register_parsers(main_subparsers, main_parser):
    parser = main_subparsers.add_parser("run", help="Run a workflow")
    workflows_yaml = load_workflows()
    variables = load_variables()
    workflows = (workflows_yaml.get("workflows") or []) if workflows_yaml is not None else []
    workflow_names = [w.get("name") for w in workflows]
    subparsers = parser.add_subparsers()
    for workflow_name in workflow_names:
        workflow_parser = subparsers.add_parser(workflow_name, help=f"Run the '{workflow_name}' workflow")

        global_variables = variables.get("global")
        if global_variables:
            for key in global_variables:
                workflow_parser.add_argument("--" + key,
                                             help=f"by default, the value is {pretty_print_variable_value(global_variables[key])}",
                                             type=str,
                                             nargs="?")
        workflow_variables = variables.get(workflow_name)
        if workflow_variables:
            for key in workflow_variables:
                workflow_parser.add_argument("--" + key,
                                             help=f"by default, the value is {pretty_print_variable_value(workflow_variables[key])}",
                                             type=str,
                                             nargs="?")

        def run_workflow(_workflow_name):
            def _run_workflow(args):
                if len(workflows) > 0:
                    try:
                        validate(workflows_yaml, yaml.load(workflows_schema_yaml, Loader=yaml.FullLoader))
                        repo_url, repo_branch, repo_hash, repo_diff = load_repo_data()
                        dstack_config = get_config()
                        # TODO: Support non-default profiles
                        profile = dstack_config.get_profile("default")

                        # TODO: Support large repo_diff
                        headers = {
                            "Content-Type": f"application/json; charset=utf-8"
                        }
                        if profile.token is not None:
                            headers["Authorization"] = f"Bearer {profile.token}"
                        variables = {k: v for (k, v) in vars(args).items() if k != "func" and v is not None}
                        data = {
                            "workflow_name": _workflow_name,
                            "repo_url": repo_url,
                            "repo_branch": repo_branch,
                            "repo_hash": repo_hash,
                            "variables": variables
                        }
                        if repo_diff:
                            data["repo_diff"] = repo_diff
                        data_bytes = json.dumps(data).encode("utf-8")
                        response = requests.request(method="POST", url=f"{profile.server}/runs/submit",
                                                    data=data_bytes,
                                                    headers=headers, verify=profile.verify)
                        if response.status_code == 200:
                            print(response.json().get("run_name"))
                        elif response.status_code == 404 and response.json().get("message") == "repo not found":
                            sys.exit("Call 'dstack init' first")
                        else:
                            response.raise_for_status()

                    except ConfigurationError:
                        sys.exit(f"Call 'dstack login' or 'dstack register' first")
                    except InvalidGitRepositoryError:
                        sys.exit(f"{os.getcwd()} is not a Git repo")
                    except ValidationError as e:
                        sys.exit(f"There a syntax error in {os.getcwd()}/.dstack/workflows.yaml:\n\n{e}")
                else:
                    sys.exit(f"No workflows defined in {os.getcwd()}/.dstack/workflows.yaml")

            return _run_workflow

        workflow_parser.set_defaults(func=run_workflow(workflow_name))

    def default_run_workflow(_: Namespace):
        parser.print_help()
        exit(1)

    parser.set_defaults(func=default_run_workflow)


def pretty_print_variable_value(obj):
    if type(obj) is str:
        return f"\"{obj}\""
    else:
        return str(obj)
