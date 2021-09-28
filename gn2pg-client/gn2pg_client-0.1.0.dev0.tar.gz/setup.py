# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gn2pg']

package_data = \
{'': ['*'], 'gn2pg': ['data/*', 'locale/fr_FR/LC_MESSAGES/import_gn.po']}

install_requires = \
['SQLAlchemy>=1.3.22,<2.0.0',
 'coloredlogs>=15.0,<16.0',
 'psycopg2-binary>=2.8.6,<3.0.0',
 'requests>=2.25.1,<3.0.0',
 'schema>=0.7.3,<0.8.0',
 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['gn2pg_cli = gn2pg.main:run']}

setup_kwargs = {
    'name': 'gn2pg-client',
    'version': '0.1.0.dev0',
    'description': 'Import tool from GeoNature to a PostgreSQL database through Export module API (client side)',
    'long_description': '**************\n GN2PG Client\n**************\n\n.. image:: https://img.shields.io/badge/python-3.7+-yellowgreen\n   :target: https://www.python.org/\n.. image:: https://img.shields.io/badge/PostgreSQL-10+-blue\n   :target: https://www.postgresql.org/\n.. image:: https://img.shields.io/badge/packaging%20tool-poetry-important\n   :target: https://python-poetry.org/\n.. image:: https://img.shields.io/badge/code%20style-black-black\n   :target: https://github.com/psf/black\n.. image:: https://img.shields.io/badge/licence-AGPL--3.0-blue\n   :target: https://opensource.org/licenses/AGPL-3.0\n.. image:: https://app.fossa.com/api/projects/git%2Bgithub.com%2Flpoaura%2FGN2PG.svg?type=shield\n   :target: https://app.fossa.com/projects/git%2Bgithub.com%2Flpoaura%2FGN2PG?ref=badge_shield\n\nThis project provides an import tool between GeoNature_ instances (client side).\nWidely inspired from `ClientApiVN <https://framagit.org/lpo/Client_API_VN/>`_\n\n\n.. contents:: Topics\n\n.. warning::\n    Actually in development.\n\n\n\n.. image:: ./docs/source/_static/src_gn2pg.png\n    :align: center\n    :alt: Project logo\n\n\nProject Setup\n=============\n\nGN2PG Client can be installed by running ``pip``. It requires Python 3.7.4# to run.\n\n.. code-block:: bash\n\n    pip install gn2pg-client\n\n\nIssues\n======\n\nPlease report any bugs or requests that you have using the `GitHub issue tracker <https://github.com/lpoaura/gn2pg_client/issues>`_!\n\nHowTo\n=====\n\nHelp\n####\n\n.. code-block:: bash\n\n    gn2pg_cli --help\n\nInit config file\n################\n\nThis command init a TOML config file within ``~/.gn2pg`` hidden directory (in user ``HOME`` directory), named as you want. PLEASE DO NOT SPECIFY PATH!\n\n.. code-block:: bash\n\n    gn2pg_cli --init <myconfigfile>\n\n\nConfig file is structured as this. ``[[source]]`` block can be duplicate as many as needed (one block for each source).\n\n.. code-block:: TOML\n\n    # GN2PG configuration file\n\n    # Local db configuration\n    [db]\n    db_host = "localhost"\n    db_port = 5432\n    db_user = "<dbUser>"\n    db_password = "<dbPassword>"\n    db_name = "<dbName>"\n    db_schema_import = "schema"\n        # Additional connection options (optional)\n        [db.db_querystring]\n        sslmode = "prefer"\n\n\n    # Source configuration,\n    # Ducplicate this block for each source (1 source = 1 export)\n    [[source]]\n    # Source name, will be use to tag stored data in import table\n    name = "Source1"\n    # GeoNature source login\n    user_name = "<monuser>"\n    # GeoNature source password\n    user_password = "<monPwd>"\n    # GeoNature source URL\n    url = "<http://geonature1/>"\n    # GeoNature source Export id\n    export_id = 1\n    # Data type is facultative. By default the value is \'synthese\'. Therefore, triggers from to_gnsynthese.sql are not activated.\n    # If you want to insert your date into a GeoNature database please choose either \'synthese_with_cd_nomenclature\' or \'synthese_with_label\'.\n    # If not, delete the line.\n    data_type = "synthese_with_cd_nomenclature"\n\n\n    [[source]]\n    # Source configuration\n    name = "Source2"\n    user_name = "<monuser>"\n    user_password = "<monPwd>"\n    url = "<http://geonature2/>"\n    export_id = 1\n    data_type = "synthese_with_cd_nomenclature"\n\n\n\n.. tip::\n\n   You can add variable in source block ``enable = false`` to disable a source\n\n\nInitDB  Schema and tables\n#########################\n\nTo create json tables where datas will be downloaded, run :\n\n.. code-block:: bash\n\n    gn2pg_cli --json-tables-create <myconfigfile>\n\n\nFull download\n#############\n\nTo download all datas from API, run :\n\n.. code-block:: bash\n\n    gn2pg_cli --full <myconfigfile>\n\nIncremental download\n####################\n\nTo update data since last download, run :\n\n.. code-block:: bash\n\n    gn2pg_cli --update <myconfigfile>\n\n\nDebug mode\n############\n\nDebug mode can be activated using ``--verbose`` CLI argument\n\nLogs\n####\n\nLog files are stored in ``$HOME/.gn2pg/log`` directory.\n\nImport datas into GeoNature datas\n#################################\n\nDefault script to auto populate GeoNature is called "to_gnsynthese".\n\n.. code-block:: bash\n\n    gn2pg_cli --custom-script to_gnsynthese <myconfigfile>\n\n\n.. tip::\n\n    You can also replacing synthese script by your own scripts, using file path instead of ``to_gnsynthese``.\n\n\nContributing\n============\n\nAll devs must be done in forks.\n\nPull requests must be pulled to `dev` branch. For example with this command:\n\n.. code-block:: bash\n\n    gh repo fork --clone lpoaura/gn2pg_client\n\n\nInstall project and development requirements (require `poetry <https://python-poetry.org/>`_):\n\n.. code-block:: bash\n\n    poetry install\n\nMake your devs and pull requests.\n\nRun `gn2pg_cli` command in dev mode\n\n.. code-block:: bash\n\n    poetry run gn2pg_cli <options>\n\nRenew requirements file for non poetry developers\n#################################################\n\n.. code-block:: bash\n\n    poetry export -f requirements.txt > requirements.txt\n\n\nLicence\n=======\n\n`GNU AGPLv3 <https://www.gnu.org/licenses/gpl.html>`_\n\nTeam\n====\n\n* `@lpofredc <https://github.com/lpofredc/>`_ (`LPO Auvergne-Rhône-Alpes <https://github.com/lpoaura/>`_), main developper\n\n\n.. image:: https://raw.githubusercontent.com/lpoaura/biodivsport-widget/master/images/LPO_AuRA_l250px.png\n    :align: center\n    :height: 100px\n    :alt: Logo LPOAuRA\n\n.. _GeoNature: https://geonature.fr/\n\n------------\n\nWith the financial support of the `DREAL Auvergne-Rhône-Alpes <http://www.auvergne-rhone-alpes.developpement-durable.gouv.fr/>`_.\n\n.. image:: https://data.lpo-aura.org/web/images/blocmarque_pref_region_auvergne_rhone_alpes_rvb_web.png\n    :align: center\n    :height: 100px\n    :alt: Logo DREAL AuRA\n',
    'author': 'lpofredc',
    'author_email': 'frederic.cloitre@lpo.fr',
    'maintainer': 'lpofredc',
    'maintainer_email': 'frederic.cloitre@lpo.fr',
    'url': 'https://github.com/lpoaura/gn2gn_client/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
