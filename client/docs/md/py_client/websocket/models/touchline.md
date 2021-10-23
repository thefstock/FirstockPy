Module py_client.websocket.models.touchline
===========================================
The model for sending touchline subscription & unsubscription request

Classes
-------

`TouchlineSubscribeModel(**data: Any)`
:   The touchline subscription request model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `t: py_client.websocket.enums.MessageTopic`
    :   Always 't' for touchline task

    `k: List[str]`
    :   One or more scriplist for subscription

    `Config`
    :   The model config

`TouchlineUnsubscribeModel(**data: Any)`
:   The touchline subscription request model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `t: py_client.websocket.enums.MessageTopic`
    :   Always 'u' for unsubscribe touchline task

    `k: List[str]`
    :   One or more scriplist for unsubscription

    `Config`
    :   The model config