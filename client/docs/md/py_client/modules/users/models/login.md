Module py_client.modules.users.models.login
===========================================
Request and Response models for login

Classes
-------

`LoginRequestModel(**data: Any)`
:   The data model for login request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `apkversion: str`
    :   Application Version

    `uid: str`
    :   User Id of the login user

    `pwd: Optional[pydantic.types.SecretStr]`
    :   password for login. It will be automatically hashed during the request

    `dpin: Optional[pydantic.types.SecretStr]`
    :   The device pin

    `factor2: Union[datetime.date, str]`
    :   DOB or PAN

    `vc: str`
    :   Vendor code

    `appkey: str`
    :   Sha256 of uid|vendor_key

    `imei: str`
    :   IMEI for mobile (If desktop it takes the MAC address)

    `addldivinf: Optional[str]`
    :   Value must be in below format:
          iOS - iosInfo.utsname.machine - iosInfo.systemVersion
          Android - androidInfo.model - androidInfo.version
        examples:
          iOS - iPhone 8.0 - 9.0
          Android - Moto G - 9 PKQ1.181203.01

    `ipaddr: Optional[pydantic.networks.IPvAnyAddress]`
    :   The IP address of the system

    `source: Optional[py_client.common.enums.RequestSourceType]`
    :   Access Type

    `Config`
    :   model configuration

    ### Static methods

    `validate(values: dict)`
    :   Validate the model. The model should contain either of 'pwd' or 'dpin'

`LoginResponseModel(**data: Any)`
:   The data model for login response
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   Login success or failure status

    `susertoken: Optional[str]`
    :   Present only on login success. This key is to be passed in subsequent requests

    `lastaccesstime: Optional[datetime.datetime]`
    :   Present only on login success.

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful login.

    `spasswordreset: Optional[str]`
    :   If Y Mandatory password reset to be enforced. Otherwise the field will be absent.

    `exarr: Optional[List[str]]`
    :   list of strings with enabled exchange names

    `uname: Optional[str]`
    :   Username

    `actid: Optional[str]`
    :   Account Id

    `email: Optional[pydantic.networks.EmailStr]`
    :   Email Id

    `brkname: Optional[str]`
    :   Broker Id

    `emsg: Optional[str]`
    :   Error message if the login failed

    `Config`
    :   model configuration