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

    `uid: str`
    :   User Id

    `pan: str`
    :   PAN of the user

    `dob: datetime.date`
    :   Date of birth

    `Config`
    :   model configuration

`ForgotPasswordResponseModel(**data: Any)`
:   The response model for forgot password endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   Password reset is Success Or failure status

    `request_time: datetime.datetime`
    :   Response received time

    `emsg: Optional[str]`
    :   Error message if the forgot password failed

    `Config`
    :   model configuration