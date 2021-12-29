Module py_client.modules.users.models.user_details
==================================================
Request and response models for fetching user details

Classes
-------

`UserDetailsRequestModel(**data: Any)`
:   The request model for user details endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

`UserDetailsResponseModel(**data: Any)`
:   The response model for user details endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `actid: Optional[str]`
    :   Account Id

    `brkname: Optional[str]`
    :   Broker Id

    `brnchid: Optional[str]`
    :   Branch Id

    `email: Optional[pydantic.networks.EmailStr]`
    :   Email Id

    `emsg: Optional[str]`
    :   Error message if the request failed

    `exarr: Optional[List[str]]`
    :   List of strings with enabled exchange names

    `m_num: Optional[str]`
    :   Mobile Number

    `orarr: Optional[List[str]]`
    :   List of strings with enabled price types for user

    `prarr: Optional[List[py_client.common.models.Product]]`
    :   List of Product Obj with enabled products, as defined below.

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The logout success or failure status

    `u_prev: Optional[str]`
    :   Always it will be an INVESTOR, other types of user not allowed to login using this API.