Module py_client.modules.users.models.get_hs_token
==================================================
Request and response models for get HS token request

Classes
-------

`GetHsTokenRequestModel(**data: Any)`
:   The request model for get HS token endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :

`GetHsTokenResponseModel(**data: Any)`
:   The response model for get HS token endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `emsg: Optional[str]`
    :   Error message if the request failed

    `hstk: Optional[str]`
    :   One time Token to be sent to BackOffice or third party link

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The logout success or failure status