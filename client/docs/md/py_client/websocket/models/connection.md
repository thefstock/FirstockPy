Module py_client.websocket.models.connection
============================================
The model for sending connection request

Classes
-------

`WebsocketConnectionModel(**data: Any)`
:   The connection request model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `actid: str`
    :   Account id

    `source: py_client.common.enums.RequestSourceType`
    :   Source should be same as login request.

    `susertoken: Optional[str]`
    :   User Session Token

    `t: py_client.websocket.enums.MessageTopic`
    :   The message topic

    `uid: str`
    :   User ID