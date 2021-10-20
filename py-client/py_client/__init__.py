"""
The py_client library abstracts away the REST communication logic by exposing a set of classes and
methods to effectively execute the tasks.

Library exposes a **Client** which abstracts the underlying logic by providing methods and submodules
to communicate with the server.

```py
from py_client import Client, LoginRequestModel, HttpException

client = Client(base_url='http://<HOST>:<PORT>')

login_model = LoginRequestModel(...)

try:
  response = client.login(login_model)
  print('Success')
  print(response.json(exclude_unset=True))
except HttpException as e:
  print('Failed: ', e.reason)
except:
  print('Connection failed')
```

The library uses **requests** library under the hood to interface with the REST API.
"""
__version__ = '0.1.0'

from .common import *
from .modules import *
from .utils import *
from .client import *