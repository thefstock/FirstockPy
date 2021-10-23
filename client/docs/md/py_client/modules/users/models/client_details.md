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

    `uid: str`
    :   The user id of the login user

    `actid: str`
    :   Login users account ID

    `brkname: str`
    :   Login users broker ID

`ClientDetailsResponseModel(**data: Any)`
:   The response model for client details endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The logout success or failure status

    `actid: Optional[str]`
    :   Login users account ID

    `creatdte: Optional[datetime.datetime]`
    :   Creation date

    `creattme: Optional[datetime.datetime]`
    :   Creation time

    `m_num: Optional[str]`
    :   Mobile number

    `email: Optional[pydantic.networks.EmailStr]`
    :   Email Id

    `pan: Optional[str]`
    :   The PAN of user

    `addr: Optional[str]`
    :   Address

    `addroffice: Optional[str]`
    :   Office address

    `addrcity: Optional[str]`
    :   City

    `addrstate: Optional[str]`
    :   State

    `bankdetails: Optional[List[py_client.common.models.BankDetails]]`
    :   List of bank details

    `dp_acct_num: Optional[List[py_client.common.models.DpAccountNumber]]`
    :   List of bank

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration