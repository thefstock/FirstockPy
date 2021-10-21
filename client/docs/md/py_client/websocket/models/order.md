Module py_client.websocket.models.order
=======================================
The model for sending order subscription & unsubscription request

Classes
-------

`OrderSubscribeModel(**data: Any)`
:   The order subscription request model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `actid: str`
    :   Account id based on which order updated to be sent.

    `t: py_client.websocket.enums.MessageTopic`
    :   Always 'o' for order update task

`OrderUnsubscribeModel(**data: Any)`
:   The depth subscription request model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   The model config

    `t: py_client.websocket.enums.MessageTopic`
    :   Always 'uo' for unsubscribe order update task