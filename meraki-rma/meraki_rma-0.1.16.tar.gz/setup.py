# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['meraki_rma']

package_data = \
{'': ['*']}

install_requires = \
['meraki-dashboard-connect>=0.1.1,<0.2.0',
 'meraki-env>=0.1.1,<0.2.0',
 'meraki-exception>=0.1.1,<0.2.0',
 'meraki>=1.4.3,<2.0.0',
 'rich>=10.10.0,<11.0.0',
 'typer>=0.3.2,<0.4.0']

setup_kwargs = {
    'name': 'meraki-rma',
    'version': '0.1.16',
    'description': 'Library to make Meraki RMAs easy and programmatic.',
    'long_description': '# Meraki RMA Wrapper\n\nThis repo contains an early prototype to simplify replacing devices on the Meraki Dashboard.\n\n\n## Insallation :\npip install meraki-rma / poetry add meraki-rma\n\n\n## Usage :\n\nfrom meraki_rma import MerakiRma\n\n\nthen see examples/switch-rma.py\n',
    'author': 'Thomas Christory',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/thomaschristory/meraki_rma',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
