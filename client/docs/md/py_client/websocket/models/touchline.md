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

    `Config`
    :   The model config

    `k: List[str]`
    :   One or more scriplist for subscription

    `t: py_client.websocket.enums.MessageTopic`
    :   Always 't' for touchline task

`TouchlineUnsubscribeModel(**data: Any)`
:   The touchline subscription request model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   The model config

    `k: List[str]`
    :   One or more scriplist for unsubscription

    `t: py_client.websocket.enums.MessageTopic`
    :   Always 'u' for unsubscribe touchline task