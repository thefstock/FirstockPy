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

    `Config`
    :   model configuration

    `addldivinf: Optional[str]`
    :   Value must be in below format:
          iOS - iosInfo.utsname.machine - iosInfo.systemVersion
          Android - androidInfo.model - androidInfo.version
        examples:
          iOS - iPhone 8.0 - 9.0
          Android - Moto G - 9 PKQ1.181203.01

    `apkversion: str`
    :   Application Version

    `appkey: str`
    :   Sha256 of uid|vendor_key

    `dpin: Optional[pydantic.types.SecretStr]`
    :   The device pin

    `factor2: Union[datetime.date, str]`
    :   DOB or PAN

    `imei: str`
    :   IMEI for mobile (If desktop it takes the MAC address)

    `ipaddr: Optional[pydantic.networks.IPvAnyAddress]`
    :   The IP address of the system

    `pwd: Optional[pydantic.types.SecretStr]`
    :   password for login. It will be automatically hashed during the request

    `source: Optional[py_client.common.enums.RequestSourceType]`
    :   Access Type

    `uid: str`
    :   User Id of the login user

    `vc: str`
    :   Vendor code

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

    `Config`
    :   model configuration

    `actid: Optional[str]`
    :   Account Id

    `brkname: Optional[str]`
    :   Broker Id

    `email: Optional[pydantic.networks.EmailStr]`
    :   Email Id

    `emsg: Optional[str]`
    :   Error message if the login failed

    `exarr: Optional[List[str]]`
    :   list of strings with enabled exchange names

    `lastaccesstime: Optional[datetime.datetime]`
    :   Present only on login success.

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful login.

    `spasswordreset: Optional[str]`
    :   If Y Mandatory password reset to be enforced. Otherwise the field will be absent.

    `stat: py_client.common.enums.ResponseStatus`
    :   Login success or failure status

    `susertoken: Optional[str]`
    :   Present only on login success. This key is to be passed in subsequent requests

    `uname: Optional[str]`
    :   Username