## Getting Started

### Client

The client is the main access point for all operations in every module.
The client syncs the state between all the modules to use a shared application state.

#### Initialize the Client.

Initialize the client with an `api_url` and a `socket_url`

```py
import os
from py_client import Client

# We assume that the api_url and socket_url comes from env.
API_URL = os.getenv('API_URL')
SOCKET_URL = os.getenv('SOCKET_URL')

client = Client(api_url=API_URL, socket_url=SOCKET_URL)
```

> The `socket_url` is used to make the websocket connection from the client

#### Login user

Since most of the methods requires the user to login. First you should login user with the `login` method of client.
Inorder to do that we need to import the `LoginRequestModel` to encapsulate the data.

```py
from py_client.common import RequestSourceType, ResponseStatus
from py_client.models import LoginRequestModel

credentials = LoginRequestModel(
  apkversion = os.getenv('APK_VERSION'),
  appkey = os.getenv('APP_KEY'),
  vc = os.getenv('VC'),
  uid = os.getenv('UID'),
  pwd = os.getenv('PASSWORD'),
  factor2 = os.getenv('FACTOR2'),
  imei = os.getenv('imei'),
  source = RequestSourceType.API
)

response = client.login(credentials)
# response is of type `LoginResponseModel`
if response.stat == ResponseStatus.OK:
  print('Login Successful')
else:
  print('Login Failed')
  print(response.emsg)
# You can store the session token in a variable if needed
# token = response.susertoken
```

> The request and response models does a minimum level of validation and transformation to send proper data in proper format required by the server.

#### Sending Request for protected content

After logging in, now we are able to request contents that requires authentication.
These methods requires us to provide as key the `susertoken` recieved in login response.
You can store the token in a variable and reuse everywhere the key is required.
The `client` already do this under the hood by using a shared state to hold the session token and reusing it wherever necessary.

Request for user details after client login:

```py
from py_client.models import UserDetailsRequestModel

model = UserDetailsRequestModel(uid=self.args.uid)
details = client.users.user_details(model)
# The user details method also takes an optional `key` argument.
# to provide the session token in case login request is not done by the client.
```

#### Logout

To logout a logged in user, use the `logout` method of the client.
This sends a logout request to the server and also clears the session token from client state.

```py
response = client.logout()
if response.stat == ResponseStatus.OK:
  print('Logout successful')
else:
  print('Logout Failed')
  print(response.emsg)
```

### Websockets

The master client also manages a websocket client to handle websocket requests.
The master client shares its state with the websocket client.
The websocket connection is not made by the client.
This is to avoid making unnecessary connections where websocket operations might not be required.

The websocket client is decoupled from the master client but is kept as part of the master client to abstract the state management.

To start using websockets, first we need to [initialize the client](#initialize-the-client) and complete a [login](#login-user) request.

#### Creating the connection

```py
# ... imports
# ... initialize client
# ... login

ws = client.ws

ws.connect(uid=os.getenv('UID'), actid=os.getenv('ACTID'))
ws.run_forever()
```

#### Adding event handlers

Just creating the connection does not serve the purpose of the websocket. We should be able to send and recieve messages.

The websocket client exposes three decorator methods to listen to events on the websocket:
- `on_connect` : Runs once the connection is made and ack is recieved.
- `on_message(topic)`: Runs when a message is recieved on the given topic.
- `on_close`: Runs once the connection is closed.

Let's add an on_connect listener to our websocket client

```py
ws = client.ws

# the event handlers are added before the connection is made
@ws.on_connect
def connected(client, message):
  if message.get('s') == 'OK':
    print('Connected to server')

@ws.on_close
def closed(client):
  print('Closed')

ws.connect(uid=os.getenv('UID'), actid=os.getenv('ACTID'))
ws.run_forever()
```

#### Subscribing & Unsubscribing

The websocket client can be used to subscribe to multiple topics.
Once subscribed, the client recieves the updates from these topics as feeds.
When you no longer requires updates from a topic, you can also unsubscribe from these topics.

The websocket client exposes methods to subscribe and unsubscribe for the following topics:

- Touchline
  - `subscribe_touchline`
  - `unsubscribe_touchline`
- Depth
  - `subscribe_depth`
  - `unsubscribe_depth`
- Order update
  - `subscribe_order`
  - `unsubscribe_order`

```py
ws = client.ws

@ws.on_connect
def connected(client, message):
  if message.get('s') == 'OK':
    print('Connected to server')
    client.subscribe_touchline('NSE', 'NIFTY')

@ws.on_close
def closed(client):
  print('Closed')
  client.unsubscribe_toucline('NSE', 'NIFTY')

ws.connect(uid=os.getenv('UID'), actid=os.getenv('ACTID'))
ws.run_forever()
```

> **Note**: The subscriptions are always done after the connection is made to avoid packet loss.

#### Listening to messages from topics

We were able to subscribe to a topic but how to handle the incoming messages.
Every message from the server - be it acknowledgements or updates - can be handled by registering an `on_message` handler.
Unlike `on_close` and `on_connect`, the `on_message` method requires to provide a `MessageTopic` and the handler only processes the messages from that topic.

The touchline, depth and order update topics will have seperate message topics for `ACK` and `FEED`.

```py
from py_client.websocket import MessageTopic

ws = client.ws

@ws.on_connect
def connected(client, message):
  if message.get('s') == 'OK':
    print('Connected to server')
    client.subscribe_touchline('NSE', 'NIFTY')

@ws.on_close
def closed(client):
  print('Closed')
  client.unsubscribe_toucline('NSE', 'NIFTY')

@ws.on_message(MessageTopic.TOUCHLINE_SUB_ACK)
def subscribed(client, message):
  if message.get('s') == 'OK':
    print('Subscribed to touchline')

@ws.on_message(MessageTopic.TOUCHLINE_UNSUB_ACK)
def unsubscribed(client, message):
  if message.get('s') == 'OK':
    print('Unsibscribed from touchline')

@ws.on_message(MessageTopic.TOUCHLINE_FEED)
def touchline_updates(client, message):
  print(message)

ws.connect(uid=os.getenv('UID'), actid=os.getenv('ACTID'))
ws.run_forever()
```