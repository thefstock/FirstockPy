Module py_client.modules.users.models.forgot_password
=====================================================
Request and response models for forgot password

Classes
-------

`ForgotPasswordRequestModel(**data: Any)`
:   The request model for forgot password endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `dob: datetime.date`
    :   Date of birth

    `pan: str`
    :   PAN of the user

    `uid: str`
    :   User Id

`ForgotPasswordResponseModel(**data: Any)`
:   The response model for forgot password endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `emsg: Optional[str]`
    :   Error message if the forgot password failed

    `request_time: datetime.datetime`
    :   Response received time

    `stat: py_client.common.enums.ResponseStatus`
    :   Password reset is Success Or failure status