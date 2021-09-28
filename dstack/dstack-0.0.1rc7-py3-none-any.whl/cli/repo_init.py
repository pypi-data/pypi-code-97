import json
import os
import sys
from argparse import Namespace

from git import InvalidGitRepositoryError
from requests import request

from dstack.cli.common import load_repo_data
from dstack.config import get_config, ConfigurationError


def init_func(args: Namespace):
    try:
        dstack_config = get_config()
        repo_url, _, _, _ = load_repo_data()
        # TODO: Support non-default profiles
        profile = dstack_config.get_profile("default")
        print(f"Authorizing dstack to access `{repo_url}`...")
        headers = {
            "Content-Type": f"application/json; charset=utf-8"
        }
        if profile.token is not None:
            headers["Authorization"] = f"Bearer {profile.token}"
        data = {
            "repo_url": repo_url
        }
        if args.github_token is not None:
            data["github_token"] = args.github_token
        if args.private_key is not None:
            with open(args.private_key) as f:
                data["private_key"] = f.read()
        if args.passphrase is not None:
            data["passphrase"] = args.passphrase
        if args.user_name is not None:
            data["repo_user_name"] = args.user_name
        if args.password is not None:
            data["_repo_password"] = args.password
        data_bytes = json.dumps(data).encode("utf-8")
        response = request(method="POST", url=f"{profile.server}/repos/init", data=data_bytes, headers=headers,
                           verify=profile.verify)
        if response.status_code == 200:
            print("Authorizing succeeded")
        elif response.status_code == 400:
            print(response.json()["message"])
        else:
            response.raise_for_status()
    except InvalidGitRepositoryError:
        sys.exit(f"{os.getcwd()} is not a Git repo")
    except ConfigurationError:
        sys.exit(f"Call 'dstack login' or 'dstack register' first")


def register_parsers(main_subparsers):
    parser = main_subparsers.add_parser("init", help="Authorizing dstack to access a remote repository")
    parser.add_argument("--github-token", help="A GitHub personal access token", type=str, nargs="?",
                        dest="github_token")
    parser.add_argument("--private-key", help="A path to the private key file", type=str, nargs="?",
                        dest="private_key")
    parser.add_argument("--passphrase", help="Passphrase for the private key", type=str, nargs="?")
    parser.add_argument("--user", help="User name for the repository", type=str, nargs="?", dest="user_name")
    parser.add_argument("--password", help="Password for the repository", type=str, nargs="?")

    parser.set_defaults(func=init_func)
