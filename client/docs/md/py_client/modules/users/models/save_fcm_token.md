Module py_client.modules.users.models.save_fcm_token
====================================================
Request and response models for save fcm token

Classes
-------

`SaveFCMTokenRequestModel(**data: Any)`
:   The request model for logout endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

    `fcmtkn: str`
    :   FCM token collected from device

`SaveFCMTokenResponseModel(**data: Any)`
:   The response model for logout endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The logout success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration