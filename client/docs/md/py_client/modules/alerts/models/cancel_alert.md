Module py_client.modules.alerts.models.cancel_alert
===================================================
Request and response models for cancel alert request

Classes
-------

`CancelAlertRequestModel(**data: Any)`
:   The request model for cancel alert endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

    `al_id: str`
    :   Alert Id

`CancelAlertResponseModel(**data: Any)`
:   The response model for cancel alert endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: Union[py_client.common.enums.ResponseStatus, str]`
    :   The cancel alert success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `al_id: Optional[str]`
    :   Alert Id

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration