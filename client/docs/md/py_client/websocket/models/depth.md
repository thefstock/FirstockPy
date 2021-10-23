Module py_client.websocket.models.depth
=======================================
The model for sending depth subscription & unsubscription request

Classes
-------

`DepthSubscribeModel(**data: Any)`
:   The depth subscription request model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `t: py_client.websocket.enums.MessageTopic`
    :   Always 'd' for depth task

    `k: List[str]`
    :   One or more scriplist for subscription

    `Config`
    :   The model config

`DepthUnsubscribeModel(**data: Any)`
:   The depth subscription request model
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `t: py_client.websocket.enums.MessageTopic`
    :   Always 'ud' for unsubscribe depth task

    `k: List[str]`
    :   One or more scriplist for unsubscription

    `Config`
    :   The model config