Module py_client.websocket
==========================
The websocket client to connect to websocket to recieve realtime feeds.
The NorenWebsockerClient contains decorators to assign handlers for listening to messages.

These decorators include:
  - `on_message(topic)` - Runs on every message
  - `on_connect` - Runs once connection is established (Provides the connection acknowedgement message)
  - `on_close` - Runs once the connection is closed

Example:

```python
from typing import Any
from py_client.websocket import NorenWebsocketClient
from py_client import Client, LoginRequestModel, RequestSourceType
import os
from dotenv import load_dotenv

from py_client.websocket.enums import MessageTopic

load_dotenv()

client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
ws = client.ws

# login
login_model = LoginRequestModel(
  apkversion = os.getenv('APK_VERSION'),
  appkey = os.getenv('APP_KEY'),
  vc = os.getenv('VC'),
  uid = os.getenv('UID'),
  pwd = os.getenv('PASSWORD'),
  factor2 = os.getenv("FACTOR2"),
  imei = "134243434",
  source = RequestSourceType.API
)
client.login(login_model)

@ws.on_message(MessageTopic.TOUCHLINE_FEED)
def msg_handler(client: NorenWebsocketClient, message: Any):
  print(message)

@ws.on_connect
def cnc_handler(client: NorenWebsocketClient, message: Any):
  print(message)

ws.connect(os.getenv('UID'), os.getenv('UID'))
ws.subscribe_touchline('NSE', 'NIFTY')
# run forever
ws.run_forever()
```

> Note: It uses ws4py under the hood to connect to websocket

Sub-modules
-----------
* py_client.websocket.client
* py_client.websocket.enums
* py_client.websocket.models