from typing import Any
from py_client.websocket import NorenWebsocketClient
from py_client.common import RequestSourceType, ResponseStatus
from py_client.models import LoginRequestModel
from py_client.client import Client
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
  print("Recieving touchline feed")
  print(message)

@ws.on_message(MessageTopic.TOUCHLINE_SUB_ACK)
def msg_handler(client: NorenWebsocketClient, message: Any):
  if message.get('s') == 'OK':
    print('Subscribed to touchline feed')
  print(message)

@ws.on_connect
def cnc_handler(client: NorenWebsocketClient, message: Any):
  if message.get('s') == 'OK':
    client.subscribe_touchline('NSE', 'NIFTY')
    print('Connected to server')
  print(message)


ws.connect(os.getenv('UID'), os.getenv('UID'))
# run forever
ws.run_forever()