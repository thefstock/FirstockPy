Module py_client.utils.stateful
===============================
The base stateful class to inherit sub classes from

Classes
-------

`Stateful(initial_state: Dict[str, Any] = {})`
:   The base stateful class to inherit sub classes from
    
    Initialize the stateful class with a state

    ### Descendants

    * py_client.client.Client
    * py_client.utils.datasources.rest.datasource.RestDataSource
    * py_client.websocket.client.NorenWebsocketClient

    ### Instance variables

    `state`
    :   The current app state

    ### Methods

    `get_state(self, key: str, override: Any = None, default: Any = None) ‑> Any`
    :   Get a value from the state
        
        Args:
          key (str): The name of the state var
          override (Any): The value to override the recieved value from
          default (Any): The default value to return if key do not exist
        
        Returns:
          Any: The value

    `set_state(self, key: str, value: Any)`
    :   Set a state value
        
        Args:
          key (str): The name of the state value
          value (Any): The new value to set