Module py_client
================
The py_client library abstracts away the REST communication logic by exposing a set of classes and
methods to effectively execute the tasks.

Library exposes a **Client** which abstracts the underlying logic by providing methods and submodules
to communicate with the server.

```py
from py_client import Client, LoginRequestModel, HttpException

client = Client(api_url=API_URL, socket_url=SOCKET_URL)

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

#### Data Sources / Modules

The client comprises of datasources/modules to group the available methods.
All the available datasources can be accessed from client by the corresponding property:

| Property   | Data Source                                                   |
| ---------- | ------------------------------------------------------------- |
| alerts     | `py_client.modules.alerts.datasource.AlertsDataSource`        |
| funds      | `py_client.modules.funds.datasource.FundsDataSource`          |
| markets    | `py_client.modules.markets.datasource.MarketsDataSource`      |
| orders     | `py_client.modules.orders.datasource.OrdersDataSource`        |
| users      | `py_client.modules.users.datasource.UserDataSource`           |
| watchlists | `py_client.modules.watchlists.datasource.WatchListDataSource` |

**Example:**
```py
# To access the `get_index_list` method of `MarketsDataSource`, we can use:
indexes = client.markets.get_index_list(...)
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

Sub-modules
-----------
* py_client.client
* py_client.common
* py_client.models
* py_client.modules
* py_client.utils
* py_client.websocket

Classes
-------

`AlertsDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   Datasource for handling alerts operations
    
    Initialize the RestDataSource
    
    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.

    ### Ancestors (in MRO)

    * py_client.utils.datasources.noren.datasource.NorenRestDataSource
    * py_client.utils.datasources.rest.datasource.RestDataSource
    * py_client.utils.stateful.Stateful

    ### Methods

    `cancel_alert(self, model: py_client.modules.alerts.models.cancel_alert.CancelAlertRequestModel, key: str = None) ‑> py_client.modules.alerts.models.cancel_alert.CancelAlertResponseModel`
    :   Cancel alert
        
        Args:
          model (CancelAlertRequestModel): The data to be send as CancelAlertRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          CancelAlertResponseModel: The response as CancelAlertResponseModel.

    `cancel_gtt_order(self, model: py_client.modules.alerts.models.cancel_gtt_order.CancelGttOrderRequestModel, key: str = None) ‑> py_client.modules.alerts.models.cancel_gtt_order.CancelGttOrderResponseModel`
    :   Cancel GTT order
        
        Args:
          model (CancelGttOrderRequestModel): The data to be send as CancelGttOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          CancelGttOrderResponseModel: The response as CancelGttOrderResponseModel.

    `get_enabled_alert_types(self, model: py_client.modules.alerts.models.get_enabled_alert_types.GetEnabledAlertTypesRequestModel, key: str = None) ‑> py_client.modules.alerts.models.get_enabled_alert_types.GetEnabledAlertTypesResponseModel`
    :   Get enabled alert types
        
        Args:
          model (GetEnabledAlertTypesRequestModel): The data to be send as GetEnabledAlertTypesRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetEnabledAlertTypesResponseModel: The response as GetEnabledAlertTypesResponseModel.

    `get_enabled_gtts(self, model: py_client.modules.alerts.models.get_enabled_gtts.GetEnabledGttsRequestModel, key: str = None) ‑> py_client.modules.alerts.models.get_enabled_gtts.GetEnabledGttsResponseModel`
    :   Get enabled GTTs
        
        Args:
          model (GetEnabledGttsRequestModel): The data to be send as GetEnabledGttsRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetEnabledGttsResponseModel: The response as GetEnabledGttsResponseModel.

    `get_pending_alert(self, model: py_client.modules.alerts.models.get_pending_alert.GetPendingAlertRequestModel, key: str = None) ‑> py_client.modules.alerts.models.get_pending_alert.GetPendingAlertResponseModel`
    :   Get pending alert
        
        Args:
          model (GetPendingAlertRequestModel): The data to be send as GetPendingAlertRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetPendingAlertResponseModel: The response as GetPendingAlertResponseModel.

    `get_pending_gtt_order(self, model: py_client.modules.alerts.models.get_pending_gtt_order.GetPendingGttOrderRequestModel, key: str = None) ‑> py_client.modules.alerts.models.get_pending_gtt_order.GetPendingGttOrderResponseModel`
    :   Get pending GTT order
        
        Args:
          model (GetPendingGttOrderRequestModel): The data to be send as GetPendingGttOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetPendingGttOrderResponseModel: The response as GetPendingGttOrderResponseModel.

    `get_unsettled_trading_date(self, model: py_client.modules.alerts.models.get_unsettled_trading_date.GetUnsettledTradingDateRequestModel, key: str = None) ‑> py_client.modules.alerts.models.get_unsettled_trading_date.GetUnsettledTradingDateResponseModel`
    :   Get unsettled trading date
        
        Args:
          model (GetUnsettledTradingDateRequestModel): The data to be send as GetUnsettledTradingDateRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetUnsettledTradingDateResponseModel: The response as GetUnsettledTradingDateResponseModel.

    `modify_alert(self, model: py_client.modules.alerts.models.modify_alert.ModifyAlertRequestModel, key: str = None) ‑> py_client.modules.alerts.models.modify_alert.ModifyAlertResponseModel`
    :   Modify alert
        
        Args:
          model (ModifyAlertRequestModel): The data to be send as ModifyAlertRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ModifyAlertResponseModel: The response as ModifyAlertResponseModel.

    `modify_gtt_order(self, model: py_client.modules.alerts.models.modify_gtt_order.ModifyGttOrderRequestModel, key: str = None) ‑> py_client.modules.alerts.models.modify_gtt_order.ModifyGttOrderResponseModel`
    :   Modify GTT order
        
        Args:
          model (ModifyGttOrderRequestModel): The data to be send as ModifyGttOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ModifyGttOrderResponseModel: The response as ModifyGttOrderResponseModel.

    `place_gtt_order(self, model: py_client.modules.alerts.models.place_gtt_order.PlaceGttOrderRequestModel, key: str = None) ‑> py_client.modules.alerts.models.place_gtt_order.PlaceGttOrderResponseModel`
    :   Place GTT order
        
        Args:
          model (PlaceGttOrderRequestModel): The data to be send as PlaceGttOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          PlaceGttOrderResponseModel: The response as PlaceGttOrderResponseModel.

    `set_alert(self, model: py_client.modules.alerts.models.set_alert.SetAlertRequestModel, key: str = None) ‑> py_client.modules.alerts.models.set_alert.SetAlertResponseModel`
    :   Set alert
        
        Args:
          model (SetAlertRequestMode l): The data to be send as SetAlertRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SetAlertResponseModel: The response as SetAlertResponseModel.

`Client(api_url: str, socket_url: str)`
:   The python client for communicating with external api
    
    Initialize the client
    
    Args:
      base_url (str, optional): The base url for the rest api endpoint. Defaults to None.

    ### Ancestors (in MRO)

    * py_client.utils.stateful.Stateful

    ### Instance variables

    `alerts: py_client.modules.alerts.datasource.AlertsDataSource`
    :   The alerts module datasource

    `funds: py_client.modules.funds.datasource.FundsDataSource`
    :   The funds module datasource.

    `markets: py_client.modules.markets.datasource.MarketsDataSource`
    :   The markets module datasource

    `orders: py_client.modules.orders.datasource.OrdersDataSource`
    :   The orders module datasource

    `state`
    :   The current client state

    `users: py_client.modules.users.datasource.UserDataSource`
    :   The user module datasource

    `watchlists: py_client.modules.watchlists.datasource.WatchListDataSource`
    :   The watchlists module datasource

    `ws: py_client.websocket.client.WsClient`
    :   The websocket client

    ### Methods

    `holdings(self, model: py_client.modules.holdings_limits.models.holdings.HoldingsRequestModel, key: str = None)`
    :   Get holdings
        
        Args:
          model (HoldingsRequestModel): The data to be send as HoldingsRequestModel.
          key (str): The key obtained on login success
        
        Returns:
          HoldingsResponseModel: The response as HoldingsResponseModel.

    `limits(self, model: py_client.modules.holdings_limits.models.limits.LimitsRequestModel, key: str = None)`
    :   Limits
        
        Args:
          model (LimitsRequestModel): The data to be send as LimitsRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          LimitsResponseModel: The response as LimitsResponseModel.

    `login(self, model: py_client.modules.users.models.login.LoginRequestModel)`
    :   Login user. Alias for ```client.users.login```
        
        Args:
          model (LoginRequestModel): The data to be send as LoginRequestModel instance.
        
        Returns:
          LoginResponseModel: The response from login request as LoginResponseModel instance.

    `logout(self, model: py_client.modules.users.models.logout.LogoutRequestModel, key: str = None)`
    :   Logout user. Alias for ```client.users.logout```
        
        Args:
          model (LogoutRequestModel): The data to be send as LogoutRequestModel instance
          key (str): The key obtained on login success
        
        Returns:
          LogoutResponseModel: The response from logout request as LogoutResponseModel instance

`FundsDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   Datasource for handling funds operations
    
    Initialize the RestDataSource
    
    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.

    ### Ancestors (in MRO)

    * py_client.utils.datasources.noren.datasource.NorenRestDataSource
    * py_client.utils.datasources.rest.datasource.RestDataSource
    * py_client.utils.stateful.Stateful

    ### Methods

    `get_content_basket(self, model: py_client.modules.funds.models.get_content_basket.GetContentBasketRequestModel, key: str = None) ‑> py_client.modules.funds.models.get_content_basket.GetContentBasketResponseModel`
    :   Get content basket
        
        Args:
          model (GetContentBasketRequestModel): The data to be send as GetContentBasketRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetContentBasketResponseModel: The response as GetContentBasketResponseModel.

    `get_content_list(self, model: py_client.modules.funds.models.get_content_list.GetContentListRequestModel, key: str = None) ‑> py_client.modules.funds.models.get_content_list.GetContentListResponseModel`
    :   Get content list
        
        Args:
          model (GetContentListRequestModel): The data to be send as GetContentListRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetContentListResponseModel: The response as GetContentListResponseModel.

    `get_max_payout_amount(self, model: py_client.modules.funds.models.get_max_payout_amount.GetMaxPayoutAmountRequestModel, key: str = None) ‑> py_client.modules.funds.models.get_max_payout_amount.GetMaxPayoutAmountResponseModel`
    :   Get max payout amount
        
        Args:
          model (GetMaxPayoutAmountRequestModel): The data to be send as GetMaxPayoutAmountRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetMaxPayoutAmountResponseModel: The response as GetMaxPayoutAmountResponseModel.

`MarketsDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   Datasource for handling markets operations
    
    Initialize the RestDataSource
    
    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.

    ### Ancestors (in MRO)

    * py_client.utils.datasources.noren.datasource.NorenRestDataSource
    * py_client.utils.datasources.rest.datasource.RestDataSource
    * py_client.utils.stateful.Stateful

    ### Methods

    `exch_msg(self, model: py_client.modules.markets.models.exch_message.ExchMessageRequestModel, key: str = None) ‑> py_client.modules.markets.models.exch_message.ExchMessageResponseModel`
    :   Exch message
        
        Args:
          model (ExchMessageRequestModel): The data to be send as ExchMessageRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ExchMessageResponseModel: The response as ExchMessageResponseModel.

    `get_broker_msg(self, model: py_client.modules.markets.models.get_broker_message.GetBrokerMessageRequestModel, key: str = None) ‑> py_client.modules.markets.models.get_broker_message.GetBrokerMessageResponseModel`
    :   Get broker message
        
        Args:
          model (GetBrokerMessageRequestModel): The data to be send as GetBrokerMessageRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetBrokerMessageResponseModel: The response as GetBrokerMessageResponseModel.

    `get_index_list(self, model: py_client.modules.markets.models.get_index_list.GetIndexListRequestModel, key: str = None) ‑> py_client.modules.markets.models.get_index_list.GetIndexListResponseModel`
    :   Get index list
        
        Args:
          model (GetIndexListRequestModel): The data to be send as GetIndexListRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetIndexListResponseModel: The response as GetIndexListResponseModel.

    `get_option_chain(self, model: py_client.modules.markets.models.get_option_chain.GetOptionChainRequestModel, key: str = None) ‑> py_client.modules.markets.models.get_option_chain.GetOptionChainResponseModel`
    :   Get option chain
        
        Args:
          model (GetOptionChainRequestModel): The data to be send as GetOptionChainRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetOptionChainResponseModel: The response as GetOptionChainResponseModel.

    `span_calc(self, model: py_client.modules.markets.models.span_calculator.SpanCalculatorRequestModel, key: str = None) ‑> py_client.modules.markets.models.span_calculator.SpanCalculatorResponseModel`
    :   Get broker message
        
        Args:
          model (SpanCalculatorRequestModel): The data to be send as SpanCalculatorRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SpanCalculatorResponseModel: The response as SpanCalculatorResponseModel.

    `top_list(self, model: py_client.modules.markets.models.top_list.TopListRequestModel, key: str = None) ‑> py_client.modules.markets.models.top_list.TopListResponseModel`
    :   Get top list
        
        Args:
          model (TopListRequestModel): The data to be send as TopListRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          TopListResponseModel: The response as TopListResponseModel.

    `top_list_names(self, model: py_client.modules.markets.models.top_list_names.TopListNamesRequestModel, key: str = None) ‑> py_client.modules.markets.models.top_list_names.TopListNamesResponseModel`
    :   Get top list names
        
        Args:
          model (TopListNamesRequestModel): The data to be send as TopListNamesRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          TopListNamesResponseModel: The response as TopListNamesResponseModel.

    `tp_series(self, model: py_client.modules.markets.models.time_price_series.TimePriceSeriesRequestModel, key: str = None) ‑> py_client.modules.markets.models.time_price_series.TimePriceSeriesResponseModel`
    :   Get time price data (Chart data)
        
        Args:
          model (TimePriceSeriesRequestModel): The data to be send as TimePriceSeriesRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          TimePriceSeriesResponseModel: The response as TimePriceSeriesResponseModel.

`OrdersDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   The datasource for all order specific requests
    
    Initialize the RestDataSource
    
    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.

    ### Ancestors (in MRO)

    * py_client.utils.datasources.noren.datasource.NorenRestDataSource
    * py_client.utils.datasources.rest.datasource.RestDataSource
    * py_client.utils.stateful.Stateful

    ### Methods

    `cancel_order(self, model: py_client.modules.orders.models.cancel_order.CancelOrderRequestModel, key: str = None) ‑> py_client.modules.orders.models.cancel_order.CancelOrderResponseModel`
    :   Cancel order
        
        Args:
          model (CancelOrderRequestModel): The data to be send as CancelOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          CancelOrderResponseModel: The response as CancelOrderResponseModel.

    `convert_product(self, model: py_client.modules.orders.models.convert_product.ConvertProductRequestModel, key: str = None) ‑> py_client.modules.orders.models.convert_product.ConvertProductResponseModel`
    :   Convert Product
        
        Args:
          model (ConvertProductRequestModel): The data to be send as ConvertProductRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ConvertProductResponseModel: The response as ConvertProductResponseModel.

    `exit_sno_order(self, model: py_client.modules.orders.models.exit_sno_order.ExitSnoOrderRequestModel, key: str = None) ‑> py_client.modules.orders.models.exit_sno_order.ExitSnoOrderResponseModel`
    :   Exit sno order
        
        Args:
          model (ExitSnoOrderRequestModel): The data to be send as ExitSnoOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ExitSnoOrderResponseModel: The response as ExitSnoOrderResponseModel.

    `get_basket_margin(self, model: py_client.modules.orders.models.get_basket_margin.GetBasketMarginRequestModel, key: str = None) ‑> py_client.modules.orders.models.get_basket_margin.GetBasketMarginResponseModel`
    :   Get basket margin
        
        Args:
          model (GetBasketMarginRequestModel): The data to be send as GetBasketMarginRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetBasketMarginResponseModel: The response as GetBasketMarginResponseModel.

    `get_order_margin(self, model: py_client.modules.orders.models.get_order_margin.GetOrderMarginRequestModel, key: str = None) ‑> py_client.modules.orders.models.get_order_margin.GetOrderMarginResponseModel`
    :   Get order margin
        
        Args:
          model (GetOrderMarginRequestModel): The data to be send as GetOrderMarginRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetOrderMarginResponseModel: The response as GetOrderMarginResponseModel.

    `modify_order(self, model: py_client.modules.orders.models.modify_order.ModifyOrderRequestModel, key: str = None) ‑> py_client.modules.orders.models.modify_order.ModifyOrderResponseModel`
    :   Modify an order
        
        Args:
          model (ModifyOrderRequestModel): The data to be send as ModifyOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ModifyOrderResponseModel: The response as ModifyOrderResponseModel.

    `multileg_order_book(self, model: py_client.modules.orders.models.multileg_order_book.MultilegOrderBookRequestModel, key: str = None) ‑> py_client.modules.orders.models.multileg_order_book.MultilegOrderBookResponseModel`
    :   Multi Leg Order book
        
        Args:
          model (MultilegOrderBookRequestModel): The data to be send as MultilegOrderBookRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          MultilegOrderBookResponseModel: The response as MultilegOrderBookResponseModel.

    `order_book(self, model: py_client.modules.orders.models.order_book.OrderBookRequestModel, key: str = None) ‑> py_client.modules.orders.models.order_book.OrderBookResponseModel`
    :   Order book
        
        Args:
          model (OrderBookRequestModel): The data to be send as OrderBookRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          OrderBookResponseModel: The response as OrderBookResponseModel.

    `place_order(self, model: py_client.modules.orders.models.place_order.PlaceOrderRequestModel, key: str = None) ‑> py_client.modules.orders.models.place_order.PlaceOrderResponseModel`
    :   Place a new order
        
        Args:
          model (PlaceOrderRequestModel): The data to be send as PlaceOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          PlaceOrderResponseModel: The response as PlaceOrderResponseModel.

    `position_book(self, model: py_client.modules.orders.models.position_book.PositionBookRequestModel, key: str = None) ‑> py_client.modules.orders.models.position_book.PositionBookResponseModel`
    :   Position Book
        
        Args:
          model (PositionBookRequestModel): The data to be send as PositionBookRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          PositionBookResponseModel: The response as PositionBookResponseModel.

    `single_order_history(self, model: py_client.modules.orders.models.single_order_history.SingleOrderHistoryRequestModel, key: str = None) ‑> py_client.modules.orders.models.single_order_history.SingleOrderHistoryResponseModel`
    :   Single Order History
        
        Args:
          model (SingleOrderHistoryRequestModel): The data to be send as SingleOrderHistoryRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SingleOrderHistoryResponseModel: The response as SingleOrderHistoryResponseModel.

    `trade_book(self, model: py_client.modules.orders.models.trade_book.TradeBookRequestModel, key: str = None) ‑> py_client.modules.orders.models.trade_book.TradeBookResponseModel`
    :   Trade Book
        
        Args:
          model (TradeBookRequestModel): The data to be send as TradeBookRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          TradeBookResponseModel: The response as TradeBookResponseModel.

`UserDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   The data source for all login/logout and user requests.
    
    Initialize the RestDataSource
    
    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.

    ### Ancestors (in MRO)

    * py_client.utils.datasources.noren.datasource.NorenRestDataSource
    * py_client.utils.datasources.rest.datasource.RestDataSource
    * py_client.utils.stateful.Stateful

    ### Methods

    `change_password(self, model: py_client.modules.users.models.change_password.ChangePasswordRequestModel) ‑> py_client.modules.users.models.change_password.ChangePasswordResponseModel`
    :   Change current password
        
        Args:
          model (ChangePasswordRequestModel): The data to be sand as ChangePasswordRequestModel
        
        Returns:
          ChangePasswordResponseModel: The response as ForgotPasswordResponseModel.

    `client_details(self, model: py_client.modules.users.models.client_details.ClientDetailsRequestModel, key: str = None) ‑> py_client.modules.users.models.client_details.ClientDetailsResponseModel`
    :   Fetch client details for the logged in user
        
        Args:
          model (ClientDetailsRequestModel): The data to be send as ClientDetailsRequestModel
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ClientDetailsResponseModel: The response as ClientDetailsResponseModel.

    `forgot_password(self, model: py_client.modules.users.models.forgot_password.ForgotPasswordRequestModel) ‑> py_client.modules.users.models.forgot_password.ForgotPasswordResponseModel`
    :   Send a forgot password request to reset password
        
        Args:
          model (ForgotPasswordRequestModel): The data to be send as ForgotPasswordRequestModel.
        
        Returns:
          ForgotPasswordResponseModel: The response from forgot password request as ForgotPasswordResponseModel.

    `get_hs_token(self, model: py_client.modules.users.models.get_hs_token.GetHsTokenRequestModel, key: str = None) ‑> py_client.modules.users.models.get_hs_token.GetHsTokenResponseModel`
    :   Get one time hs token
        
        Args:
          model (GetHsTokenRequestModel): The data to be send as GetHsTokenRequestModel
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetHsTokenResponseModel: The response as GetHsTokenResponseModel.

    `login(self, model: py_client.modules.users.models.login.LoginRequestModel) ‑> py_client.modules.users.models.login.LoginResponseModel`
    :   Login to the system using password or device pin.
          - If model contains the 'pwd' value login using normal login request.
          - If model contains the 'dpin' value login using device pin login request.
        
        Args:
          model (LoginRequestModel): The data to be send as LoginRequestModel.
        
        Returns:
          LoginResponseModel: The response from login request as LoginResponseModel.

    `logout(self, model: py_client.modules.users.models.logout.LogoutRequestModel, key: str = None) ‑> py_client.modules.users.models.logout.LogoutResponseModel`
    :   Logout the user
        
        Args:
          model (LogoutRequestModel): The data to be send as LogoutRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          LogoutResponseModel: The response from logout request as LogoutResponseModel.

    `save_fcm_token(self, model: py_client.modules.users.models.save_fcm_token.SaveFCMTokenRequestModel, key: str = None) ‑> py_client.modules.users.models.save_fcm_token.SaveFCMTokenResponseModel`
    :   Send request to save FCM token
        
        Args:
          model (SaveFCMTokenRequestModel): The data to be send as SaveFCMTokenRequestModel
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SaveFCMTokenResponseModel: The response as SaveFCMTokenResponseModel.

    `set_device_pin(self, model: py_client.modules.users.models.set_device_pin.SetDevicePinRequestModel, key: str = None) ‑> py_client.modules.users.models.set_device_pin.SetDevicePinResponseModel`
    :   Set device pin
        
        Args:
          model (SetDevicePinRequestModel): The data to be send as SetDevicePinRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SetDevicePinResponseModel: The response as SetDevicePinResponseModel.

    `user_details(self, model: py_client.modules.users.models.user_details.UserDetailsRequestModel, key: str = None) ‑> py_client.modules.users.models.user_details.UserDetailsResponseModel`
    :   Fetch details of the logged in user
        
        Args:
          model (UserDetailsRequestModel): The data to be send as UserDetailsRequestModel
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          UserDetailsResponseModel: The response as UserDetailsResponseModel.

    `validate_hs_token(self, login_id: str, token: str) ‑> bool`
    :   Check if the given HS token is valid or not
        
        Args:
          login_id (str): The sLoginId received from Initiator site,
          token (str): The HS token obtained
        
        Returns:
          bool: Whether the given token is valid or not

`WatchListDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   The datasource for all watch list specific requests
    
    Initialize the RestDataSource
    
    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.

    ### Ancestors (in MRO)

    * py_client.utils.datasources.noren.datasource.NorenRestDataSource
    * py_client.utils.datasources.rest.datasource.RestDataSource
    * py_client.utils.stateful.Stateful

    ### Methods

    `add_scrips(self, model: py_client.modules.watchlists.models.add_scrips.AddScripsRequestModel, key: str = None) ‑> py_client.modules.watchlists.models.add_scrips.AddScripsResponseModel`
    :   Add multiple scrips to a watchlist
        
        Args:
          model (AddScripsRequestModel): The data to be send as AddScripsRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          AddScripsResponseModel: The response as AddScripsResponseModel.

    `delete_scrips(self, model: py_client.modules.watchlists.models.delete_scrips.DeleteScripsRequestModel, key: str = None) ‑> py_client.modules.watchlists.models.delete_scrips.DeleteScripsResponseModel`
    :   Delete scrips from a watchlist
        
        Args:
          model (DeleteScripsRequestModel): The data to be send as DeleteScripsRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          DeleteScripsResponseModel: The response as DeleteScripsResponseModel.

    `get_names(self, model: py_client.modules.watchlists.models.get_names.GetWatchListNamesRequestModel, key: str = None) ‑> py_client.modules.watchlists.models.get_names.GetWatchListNamesResponseModel`
    :   Fetch watchlist names
        
        Args:
          model (GetWatchListNamesRequestModel): The data to be send as GetWatchListNamesRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetWatchListNamesResponseModel: The response as GetWatchListNamesResponseModel.

    `get_predefined_scrips(self, model: py_client.modules.watchlists.models.get_predefined_scrips.GetPredefinedScripsRequestModel, key: str = None) ‑> py_client.modules.watchlists.models.get_predefined_scrips.GetPredefinedScripsResponseModel`
    :   Get list of predefined MW scrips
        
        Args:
          model (GetPredefinedScripsRequestModel): The data to be send as GetPredefinedScripsRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetPredefinedScripsResponseModel: The response as GetPredefinedScripsResponseModel.

    `get_predefined_watchlists(self, model: py_client.modules.watchlists.models.get_predefined_watchlists.GetPredefinedWatchListsRequestModel, key: str = None) ‑> py_client.modules.watchlists.models.get_predefined_watchlists.GetPredefinedWatchListsResponseModel`
    :   Get list of predefined MWs
        
        Args:
          model (GetPredefinedWatchListsRequestModel): The data to be send as GetPredefinedWatchListsRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetPredefinedWatchListsResponseModel: The response as GetPredefinedWatchListsResponseModel.

    `get_quotes(self, model: py_client.modules.watchlists.models.get_quotes.GetQuotesRequestModel, key: str = None) ‑> py_client.modules.watchlists.models.get_quotes.GetQuotesResponseModel`
    :   Get quotes
        
        Args:
          model (GetQuotesRequestModel): The data to be send as GetQuotesRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetQuotesResponseModel: The response as GetQuotesResponseModel.

    `get_security_info(self, model: py_client.modules.watchlists.models.get_security_info.GetSecurityInfoRequestModel, key: str = None) ‑> py_client.modules.watchlists.models.get_security_info.GetSecurityInfoResponseModel`
    :   Get security info
        
        Args:
          model (GetSecurityInfoRequestModel): The data to be send as GetSecurityInfoRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetSecurityInfoResponseModel: The response as GetSecurityInfoResponseModel.

    `get_watchlist(self, model: py_client.modules.watchlists.models.get_watchlist.GetWatchListRequestModel, key: str = None) ‑> py_client.modules.watchlists.models.get_watchlist.GetWatchListResponseModel`
    :   Get scrip list for a given watchlist name
        
        Args:
          model (GetWatchListRequestModel): The data to be send as GetWatchListRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetWatchListResponseModel: The response as GetWatchListResponseModel.

    `search_scrips(self, model: py_client.modules.watchlists.models.search_scrips.SearchScripsRequestModel, key: str = None) ‑> py_client.modules.watchlists.models.search_scrips.SearchScripsResponseModel`
    :   Search for scrips
        
        Args:
          model (SearchScripsRequestModel): The data to be send as SearchScripsRequestModel.
          key (str): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SearchScripsResponseModel: The response as SearchScripsResponseModel.

`WsClient(url: str, state: Dict[str, Any] = {})`
:   The websocket client for realtime data
    
    Initialize the websocket client
    
    Args:
        url (str): The socket url
        state (Dict[str, Any], optional): The shared state from main client. Defaults to {}.

    ### Ancestors (in MRO)

    * ws4py.client.threadedclient.WebSocketClient
    * ws4py.client.WebSocketBaseClient
    * ws4py.websocket.WebSocket
    * py_client.utils.stateful.Stateful

    ### Methods

    `closed(self)`
    :   This method runs once the connection is closed.
        ..warning:: Do not call this method directly

    `connect(self, uid: str, actid: str)`
    :   Connect to websocket
        
        Args:
            uid (str): The user id for the user
            actid (str): The account id for the user

    `on_close(self, handler: Callable[[ForwardRef('WsClient')], None])`
    :   Add on close handler
        
        Args:
          handler (Callable[[WsClient], None]): The handler to run on connection closed
        
        Usage:
          Should be used as decorator
          ```python
          @ws.on_close
          def on_close(client):
            print('Connection closed')
          ```

    `on_connect(self, handler: Callable[[ForwardRef('WsClient'), Dict[str, Any]], None])`
    :   Add on open handler
        
        Args:
          handler (Callable[[WsClient, Dict[str, Any]], None]): The handler to run on connection opened
        
        Usage:
          Should be used as decorator
          ```python
          @ws.on_connect
          def on_connect(client, ack: Dict[str, Any]):
            print('Connected: ', ack)
          ```

    `on_message(self, topic: py_client.websocket.enums.MessageTopic)`
    :   Add on close handler
        
        Args:
          topic (MessageTopic): The handler to run when a new message is recieved
        
        Returns:
          Callable[[Callable[['WsClient', Dict[str, Any]], None]], None]
        
        Usage:
          Should be used as decorator
          ```python
          @ws.on_message(MessageTopic.DEPTH_FEED)
          def on_depth_feed(client, message: Dict[str, Any]):
            print(message)
          ```

    `opened(self)`
    :   This method runs once the connection is established
        ..warning:: Do not call this method directly

    `received_message(self, message: ws4py.messaging.TextMessage)`
    :   This method runs for every message
        ..warning:: Do not call this method directly

    `subscribe_depth(self, *scriplists: List[str])`
    :   Subscribe to depth feed
        
        Args:
          scriplists (List[str]): One or more scriplists

    `subscribe_order(self, actid: str)`
    :   Subscribe to depth feed
        
        Args:
          actid (str): Account id based on which order updated to be sent.

    `subscribe_touchline(self, *scriplists: List[str])`
    :   Subscribe to touchline feed
        
        Args:
          scriplists (List[str]): One or more scriplists

    `unsubscribe_depth(self, *scriplists: List[str])`
    :   Unsubscribe from depth feed
        
        Args:
          scriplists (List[str]): One or more scriplists

    `unsubscribe_order(self, actid: str)`
    :   Unsubscribe from depth feed
        
        Args:
          actid (str): Account id based on which order updated to be sent.

    `unsubscribe_touchline(self, *scriplists: List[str])`
    :   Unsubscribe from touchline feed
        
        Args:
          scriplists (List[str]): One or more scriplists