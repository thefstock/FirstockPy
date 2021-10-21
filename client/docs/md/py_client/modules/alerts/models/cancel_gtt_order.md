Module py_client.modules.alerts.models.cancel_gtt_order
=======================================================
Request and response models for cancel gtt order request

Classes
-------

`CancelGttOrderRequestModel(**data: Any)`
:   The request model for cancel gtt order endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `al_id: str`
    :   Alert Id

    `uid: Optional[str]`
    :   The user id of the login user

`CancelGttOrderResponseModel(**data: Any)`
:   The response model for cancel gtt order endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `al_id: Optional[str]`
    :   Alert Id

    `emsg: Optional[str]`
    :   Error message if the request failed

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The cancel gtt order success or failure status