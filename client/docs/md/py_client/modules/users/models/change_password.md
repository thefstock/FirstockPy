Module py_client.modules.users.models.change_password
=====================================================
Request and response models for change password

Classes
-------

`ChangePasswordRequestModel(**data: Any)`
:   The request model for change password endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `oldpwd: pydantic.types.SecretStr`
    :   The old password

    `pwd: str`
    :   The new password

    `uid: str`
    :   User Id

`ChangePasswordResponseModel(**data: Any)`
:   The response model for change password endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `dmsg: Optional[str]`
    :   This will be present only in case of success. Number of days to expiry will be present in same.

    `emsg: Optional[str]`
    :   Error message if password change failed

    `request_time: datetime.datetime`
    :   Response recieved time

    `stat: py_client.common.enums.ResponseStatus`
    :   Password change success or failure status