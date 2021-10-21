Module py_client.modules.users.models.client_details
====================================================
Request and Response schema for client_details request

Classes
-------

`ClientDetailsRequestModel(**data: Any)`
:   The request model for client details endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `actid: str`
    :   Login users account ID

    `brkname: str`
    :   Login users broker ID

    `uid: str`
    :   The user id of the login user

`ClientDetailsResponseModel(**data: Any)`
:   The response model for client details endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `actid: Optional[str]`
    :   Login users account ID

    `addr: Optional[str]`
    :   Address

    `addrcity: Optional[str]`
    :   City

    `addroffice: Optional[str]`
    :   Office address

    `addrstate: Optional[str]`
    :   State

    `bankdetails: Optional[List[py_client.common.models.BankDetails]]`
    :   List of bank details

    `creatdte: Optional[datetime.datetime]`
    :   Creation date

    `creattme: Optional[datetime.datetime]`
    :   Creation time

    `dp_acct_num: Optional[List[py_client.common.models.DpAccountNumber]]`
    :   List of bank

    `email: Optional[pydantic.networks.EmailStr]`
    :   Email Id

    `emsg: Optional[str]`
    :   Error message if the request failed

    `m_num: Optional[str]`
    :   Mobile number

    `pan: Optional[str]`
    :   The PAN of user

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The logout success or failure status