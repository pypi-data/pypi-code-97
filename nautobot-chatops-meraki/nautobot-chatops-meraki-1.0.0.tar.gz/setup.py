# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nautobot_plugin_chatops_meraki', 'nautobot_plugin_chatops_meraki.tests']

package_data = \
{'': ['*'], 'nautobot_plugin_chatops_meraki': ['static/nautobot_meraki/*']}

install_requires = \
['meraki>=1.7.2,<2.0.0',
 'nautobot-chatops>=1.1.0,<2.0.0',
 'typing-extensions>=3.10.0,<4.0.0']

entry_points = \
{'nautobot.workers': ['meraki = '
                      'nautobot_plugin_chatops_meraki.worker:cisco_meraki']}

setup_kwargs = {
    'name': 'nautobot-chatops-meraki',
    'version': '1.0.0',
    'description': 'Nautobot Chatops Meraki',
    'long_description': '# Cisco Meraki ChatOps\n\nUsing the [Nautobot ChatOps](https://github.com/nautobot/nautobot-plugin-chatops/) base framework, this Nautobot app (plugin) adds the ability to gather data as well as make basic changes communicating directly with the Meraki portal using Slack, Webex Teams, MS Teams, and Mattermost changing the way IT organizations support their Meraki infrastructure.\n\n## Usage\n\n### Command Setup\nAdd a slash command to Slack called `/meraki`.\nSee the [nautobot-chatops installation guide](https://github.com/nautobot/nautobot-plugin-chatops/blob/develop/docs/chat_setup/chat_setup.md) for instructions on adding a slash command to your Slack channel.\n\nYou may need to adjust your [Access Grants in Nautobot](https://github.com/nautobot/nautobot-plugin-chatops/blob/develop/docs/chat_setup/chat_setup.md#grant-access-to-the-chatbot) depending on your security requirements.\n\nThe following commands are available:\n\n- `/meraki get-organizations`:  Gather all the Meraki Organizations.\n- `/meraki get-admins [org-name]`: Based on an Organization Name Return the Admins.\n- `/meraki get-devices [org-name] [device-type]`: Gathers devices from Meraki.\n- `/meraki get-networks [org-name]`: Gathers networks from Meraki.\n- `/meraki get-switchports [org-name] [device-name]`: Gathers switch ports from a MS switch device.\n- `/meraki get-switchports-status [org-name] [device-name]`: Gathers switch ports status from a MS switch device.\n- `/meraki get-firewall-performance [org-name] [device-name]`: Query Meraki with a firewall to device performance.\n- `/meraki get-network-ssids [org-name] [net-name]`: Query Meraki for all SSIDs for a given Network.\n- `/meraki get-camera-recent [org-name] [device-name]`: Query Meraki Recent Camera Analytics.\n- `/meraki get-clients [org-name] [device-name]`: Query Meraki for List of Clients.\n- `/meraki get-lldp-cdp [org-name] [device-name]`: Query Meraki for List of LLDP or CDP Neighbors.\n- `/meraki configure-basic-access-port [org-name] [device-name] [port-number] [enabled] [vlan] [port-desc]`: Configure an access port with description, VLAN and state.\n- `/meraki cycle-port [org-name] [device-name] [port-number]`: Cycles a port on a given switch.\n\n## Screenshots\n\nRunning `/meraki get-organizations`.\n![Example output for get-organizations](docs/images/00-meraki-get-orgs.png)\n\nRunning `/meraki get-networks`.\n![Example output for get-networks](docs/images/00-meraki-get-networks.png)\n\nRunning `/meraki get-switchports-status`.\n![Example output for get-networks](docs/images/00-meraki-get-port-stats.png)\n\nSince the output was cut off the output example is below:\n```\nPort   Enabled      Status         Errors       Warnings   Speed    Duplex    Usage (Kb)    Client Count    Traffic In\n                                                                                                              (Kbps)\n========================================================================================================================\n1      True      Connected                                 1 Gbps   full     total: 46687   1              total: 4.3\n                                                                             sent: 27405                   sent: 2.5\n                                                                             recv: 19282                   recv: 1.8\n2      True      Connected                                 1 Gbps   full     total: 10086   1              total: 1.0\n                                                                             sent: 9481                    sent: 0.9\n                                                                             recv: 605                     recv: 0.1\n3      True      Disconnected   Port                                         total: 0       0              total: 0\n                                disconnected                                 sent: 0                       sent: 0\n                                                                             recv: 0                       recv: 0\n4      True      Disconnected   Port                                         total: 0       0              total: 0\n                                disconnected                                 sent: 0                       sent: 0\n                                                                             recv: 0                       recv: 0\n ```\n\nTo demonstrate a example of configuration updates.  There is a simple configuration ability for access ports.\n`/meraki configure-basic-access-port`\n\nSpecify Org, Switch, and Port ID.\n![Example output for config-port0](docs/images/00-meraki-port-config.png)\n\nFill out the Port Specific Configuration.\n![Example output for config-port1](docs/images/01-meraki-port-config.png)\n\nResult of the configuration.\n![Example output for config-port2](docs/images/02-meraki-port-config.png)\n\n## Installation\n\nThis plugin requires installation of the [Nautobot ChatOps plugin](https://github.com/nautobot/nautobot-plugin-chatops). Follow [this link](https://github.com/nautobot/nautobot-plugin-chatops/blob/develop/docs/chat_setup/chat_setup.md) to the installation instructions for that plugin.\n\nThe plugin is available as a Python package in PYPI and can be installed with pip\n\n```shell\npip install git+https://github.com/networktocode-llc/nautobot-plugin-chatops-meraki.git\n```\n\n> The plugin is compatible with Nautobot 1.0.1 and higher\n\nTo ensure Nautobot Plugin Chatops Meraki is automatically re-installed during future upgrades, create a file named `local_requirements.txt` (if not already existing) in the Nautobot root directory (alongside `requirements.txt`) and list the `nautobot-plugin-chatops-meraki` package:\n\n```no-highlight\n# echo nautobot-plugin-chatops-meraki >> local_requirements.txt\n```\n\nOnce installed, the plugin needs to be enabled in your `nautobot_config.py`\n\n```python\n# In your configuration.py\nPLUGINS = ["nautobot_chatops", "nautobot_plugin_chatops_meraki"]\n\nPLUGINS_CONFIG = {\n  "nautobot_chatops": {\n    # ADD SLACK/MS-TEAMS/WEBEX-TEAMS/MATTERMOST SETTINGS HERE\n  }\n}\n```\n> Note: There is currently no specific configuration needed for this plugin.  The only thing that is needed is below.\n\nThe plugin requires the use of a environment variable.  See below.\n\n- `MERAKI_DASHBOARD_API_KEY`: Is set to the dashboard API key. See [Meraki Dashboard API Documentation](https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API).\n\nAdd this variable and its value in the `creds.env` file.\n\n## Contributing\n\nPull requests are welcomed and automatically built and tested against multiple version of Python and multiple version of Nautobot through TravisCI.\n\nThe project is packaged with a light development environment based on `docker-compose` to help with the local development of the project and to run the tests within TravisCI.\n\nThe project is following Network to Code software development guideline and is leveraging:\n\n- Black, Pylint, Bandit and pydocstyle for Python linting and formatting.\n- Django unit test to ensure the plugin is working properly.\n\n### Development Environment\n\nThe development environment can be used in 2 ways. First, with a local poetry environment if you wish to develop outside of Docker. Second, inside of a docker container.\n\n#### Invoke tasks\n\nThe [PyInvoke](http://www.pyinvoke.org/) library is used to provide some helper commands based on the environment.  There are a few configuration parameters which can be passed to PyInvoke to override the default configuration:\n\n* `nautobot_ver`: the version of Nautobot to use as a base for any built docker containers (default: latest)\n* `project_name`: the default docker compose project name (default: nautobot-plugin-chatops-meraki)\n* `python_ver`: the version of Python to use as a base for any built docker containers (default: 3.6)\n* `local`: a boolean flag indicating if invoke tasks should be run on the host or inside the docker containers (default: False, commands will be run in docker containers)\n* `compose_dir`: the full path to a directory containing the project compose files\n* `compose_files`: a list of compose files applied in order (see [Multiple Compose files](https://docs.docker.com/compose/extends/#multiple-compose-files) for more information)\n\nUsing PyInvoke these configuration options can be overridden using [several methods](http://docs.pyinvoke.org/en/stable/concepts/configuration.html).  Perhaps the simplest is simply setting an environment variable `INVOKE_NAUTOBOT-PLUGIN-CHATOPS-MERAKI_VARIABLE_NAME` where `VARIABLE_NAME` is the variable you are trying to override.  The only exception is `compose_files`, because it is a list it must be overridden in a yaml file.  There is an example `invoke.yml` in this directory which can be used as a starting point.\n\n#### Local Poetry Development Environment\n\n1.  Copy `development/creds.env.example` to `development/creds.env` (This file will be ignored by git and docker)\n2.  Uncomment the `POSTGRES_HOST`, `REDIS_HOST`, and `NAUTOBOT_ROOT` variables in `development/creds.env`\n3.  Create an invoke.yml with the following contents at the root of the repo:\n\n```shell\n---\nnautobot_plugin_chatops_meraki:\n  local: true\n  compose_files:\n    - "docker-compose.requirements.yml"\n```\n\n3.  Run the following commands:\n\n```shell\npoetry shell\npoetry install\nexport $(cat development/dev.env | xargs)\nexport $(cat development/creds.env | xargs)\n```\n\n4.  You can now run nautobot-server commands as you would from the [Nautobot documentation](https://nautobot.readthedocs.io/en/latest/) for example to start the development server:\n\n```shell\nnautobot-server runserver 0.0.0.0:8080 --insecure\n```\n\nNautobot server can now be accessed at [http://localhost:8080](http://localhost:8080).\n\n#### Docker Development Environment\n\nThis project is managed by [Python Poetry](https://python-poetry.org/) and has a few requirements to setup your development environment:\n\n1.  Install Poetry, see the [Poetry Documentation](https://python-poetry.org/docs/#installation) for your operating system.\n2.  Install Docker, see the [Docker documentation](https://docs.docker.com/get-docker/) for your operating system.\n\nOnce you have Poetry and Docker installed you can run the following commands to install all other development dependencies in an isolated python virtual environment:\n\n```shell\npoetry shell\npoetry install\ninvoke start\n```\n\nNautobot server can now be accessed at [http://localhost:8080](http://localhost:8080).\n\n### CLI Helper Commands\n\nThe project is coming with a CLI helper based on [invoke](http://www.pyinvoke.org/) to help setup the development environment. The commands are listed below in 3 categories `dev environment`, `utility` and `testing`.\n\nEach command can be executed with `invoke <command>`. Environment variables `INVOKE_NAUTOBOT-PLUGIN-CHATOPS-MERAKI_PYTHON_VER` and `INVOKE_NAUTOBOT-PLUGIN-CHATOPS-MERAKI_NAUTOBOT_VER` may be specified to override the default versions. Each command also has its own help `invoke <command> --help`\n\n#### Docker dev environment\n\n```no-highlight\n  build            Build all docker images.\n  debug            Start Nautobot and its dependencies in debug mode.\n  destroy          Destroy all containers and volumes.\n  restart          Restart Nautobot and its dependencies.\n  start            Start Nautobot and its dependencies in detached mode.\n  stop             Stop Nautobot and its dependencies.\n```\n\n#### Utility\n\n```no-highlight\n  cli              Launch a bash shell inside the running Nautobot container.\n  create-user      Create a new user in django (default: admin), will prompt for password.\n  makemigrations   Run Make Migration in Django.\n  nbshell          Launch a nbshell session.\n```\n\n#### Testing\n\n```no-highlight\n  bandit           Run bandit to validate basic static code security analysis.\n  black            Run black to check that Python files adhere to its style standards.\n  flake8           This will run flake8 for the specified name and Python version.\n  pydocstyle       Run pydocstyle to validate docstring formatting adheres to NTC defined standards.\n  pylint           Run pylint code analysis.\n  tests            Run all tests for this plugin.\n  unittest         Run Django unit tests for the plugin.\n```\n\n## Questions\n\nFor any questions or comments, please check the [FAQ](FAQ.md) first and feel free to swing by the [Network to Code slack channel](https://networktocode.slack.com/) (channel #networktocode).\nSign up [here](http://slack.networktocode.com/)\n',
    'author': 'Network to Code, LLC',
    'author_email': 'info@networktocode.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/networktocode-llc/nautobot-plugin-chatops-meraki',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
