Module py_client.websocket.client
=================================
The websocket client

Classes
-------

`NorenWebsocketClient(url: str, state: Dict[str, Any] = {})`
:   The websocket client for accessing noren ws
    
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

    `on_close(self, handler: Callable[[ForwardRef('NorenWebsocketClient')], None])`
    :   Add on close handler
        
        Args:
          handler (Callable[[NorenWebsocketClient], None]): The handler to run on connection closed
        
        Usage:
          Should be used as decorator
          ```python
          @ws.on_close
          def on_close(client):
            print('Connection closed')
          ```

    `on_connect(self, handler: Callable[[ForwardRef('NorenWebsocketClient'), Dict[str, Any]], None])`
    :   Add on open handler
        
        Args:
          handler (Callable[[NorenWebsocketClient, Dict[str, Any]], None]): The handler to run on connection opened
        
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
          Callable[[Callable[['NorenWebsocketClient', Dict[str, Any]], None]], None]
        
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