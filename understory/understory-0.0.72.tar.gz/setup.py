# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['understory',
 'understory.apps.cache',
 'understory.apps.cache.templates',
 'understory.apps.content',
 'understory.apps.data',
 'understory.apps.debug',
 'understory.apps.jobs',
 'understory.apps.owner',
 'understory.apps.owner.templates',
 'understory.apps.search',
 'understory.apps.search.templates',
 'understory.mkdn',
 'understory.mm',
 'understory.uri',
 'understory.web',
 'understory.web.framework',
 'understory.web.framework.templates',
 'understory.web.headers',
 'understory.web.response']

package_data = \
{'': ['*'],
 'understory.apps.content': ['templates/*'],
 'understory.apps.data': ['templates/*'],
 'understory.apps.debug': ['templates/*'],
 'understory.web.framework': ['static/braid.js',
                              'static/braid.js',
                              'static/braid.js',
                              'static/braid.js',
                              'static/braid.js',
                              'static/logos/*',
                              'static/orchid.js',
                              'static/orchid.js',
                              'static/orchid.js',
                              'static/orchid.js',
                              'static/orchid.js',
                              'static/roots.js',
                              'static/roots.js',
                              'static/roots.js',
                              'static/roots.js',
                              'static/roots.js',
                              'static/solarized.css',
                              'static/solarized.css',
                              'static/solarized.css',
                              'static/solarized.css',
                              'static/solarized.css',
                              'static/understory.js',
                              'static/understory.js',
                              'static/understory.js',
                              'static/understory.js',
                              'static/understory.js']}

install_requires = \
['Pillow>=8.3.1,<9.0.0',
 'PyVirtualDisplay>=2.2,<3.0',
 'Pygments>=2.9.0,<3.0.0',
 'Unidecode>=1.2.0,<2.0.0',
 'acme-tiny>=4.1.0,<5.0.0',
 'argcomplete>=1.12.3,<2.0.0',
 'cssselect>=1.1.0,<2.0.0',
 'dnspython>=2.1.0,<3.0.0',
 'emoji>=1.2.0,<2.0.0',
 'feedparser>=6.0.8,<7.0.0',
 'gevent>=21.1.2,<22.0.0',
 'gunicorn>=20.1.0,<21.0.0',
 'hstspreload>=2021.7.5,<2022.0.0',
 'httpagentparser>=1.9.1,<2.0.0',
 'jsonpatch>=1.32,<2.0',
 'lxml>=4.6.3,<5.0.0',
 'microformats>=0.0.1,<0.0.2',
 'mimeparse>=0.1.3,<0.2.0',
 'networkx>=2.6.1,<3.0.0',
 'pendulum>=2.1.2,<3.0.0',
 'pycryptodome>=3.10.1,<4.0.0',
 'pyscreenshot>=3.0,<4.0',
 'radon>=5.0.1,<6.0.0',
 'redis>=3.5.3,<4.0.0',
 'regex>=2021.7.6,<2022.0.0',
 'requests>=2.25.1,<3.0.0',
 'rich>=10.7.0,<11.0.0',
 'scrypt>=0.8.18,<0.9.0',
 'selenium>=3.141.0,<4.0.0',
 'semver>=2.13.0,<3.0.0',
 'sh>=1.14.2,<2.0.0',
 'vobject>=0.9.6,<0.10.0',
 'watchdog>=2.1.3,<3.0.0']

entry_points = \
{'console_scripts': ['loveliness = understory.loveliness:main',
                     'web = understory.web.__main__:main']}

setup_kwargs = {
    'name': 'understory',
    'version': '0.0.72',
    'description': 'Web framework with IndieWeb support',
    'long_description': '# understory\nWeb framework with IndieWeb support\n\n## An IndieWeb-compatible personal website\n\nInstall [Poetry](https://python-poetry.org).\n\nClone your empty website repository and descend into it. *If you\nuse a **private** GitHub repository your changes will be deployed through\nGitHub. If you use a **public** repository your changes will be deployed\nthrough PyPI.*\n\nInitialize your project and add understory as a dependency.\n\n    poetry init\n    poetry add understory\n\nCreate a file `site.py`:\n\n    from understory import indieweb\n    app = indieweb.personal_site(__name__)\n\n<!--Add your site\'s app as an entry point in your `pyproject.toml`:\n\n    poetry run web install site:app AliceAnderson-->\n\nServe your website locally in development mode:\n\n    poetry run web serve site:app\n\nOpen <a href=http://localhost:9000>localhost:9000</a> in your browser.\n\n*Develop.* For example, add a custom route:\n\n    import random\n    \n    @app.route(r"hello")\n    class SayHello:\n        return random.choice(["How you doin\'?", "What\'s happening?", "What\'s up?"])\n\nTo publish:\n\n    poetry run pkg publish patch\n\nTo deploy:\n\n    poetry run gaea deploy site:app alice.anderson.example\n',
    'author': 'Angelo Gladding',
    'author_email': 'angelo@lahacker.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
