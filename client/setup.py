# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py_client',
 'py_client.common',
 'py_client.modules',
 'py_client.modules.alerts',
 'py_client.modules.alerts.models',
 'py_client.modules.funds',
 'py_client.modules.funds.models',
 'py_client.modules.holdings_limits',
 'py_client.modules.holdings_limits.models',
 'py_client.modules.markets',
 'py_client.modules.markets.models',
 'py_client.modules.orders',
 'py_client.modules.orders.models',
 'py_client.modules.users',
 'py_client.modules.users.models',
 'py_client.modules.watchlists',
 'py_client.modules.watchlists.models',
 'py_client.utils',
 'py_client.utils.datasources',
 'py_client.utils.datasources.noren',
 'py_client.utils.datasources.rest',
 'py_client.utils.interceptors',
 'py_client.websocket',
 'py_client.websocket.models']

package_data = \
{'': ['*']}

install_requires = \
['pydantic[email]>=1.8.2,<2.0.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests>=2.26.0,<3.0.0',
 'ws4py>=0.5.1,<0.6.0']

entry_points = \
{'console_scripts': ['generate = scripts.generate:main']}

setup_kwargs = {
    'name': 'py-client',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': None,
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

