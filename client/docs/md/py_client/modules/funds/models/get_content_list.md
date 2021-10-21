Module py_client.modules.funds.models.get_content_list
======================================================
Request and response models for get content list request

Classes
-------

`GetContentListRequestModel(**data: Any)`
:   The request model for get content list endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `basket: Optional[str]`
    :   Basket Name

    `condition_name: str`
    :   condition list

    `exch: str`
    :   Exchange Name

    `uid: str`
    :   The user id of the login user

`GetContentListResponseModel(**data: Any)`
:   The response model for get content list endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `ap: Optional[float]`
    :   Average trade price

    `c: Optional[float]`
    :   Close price

    `emsg: Optional[str]`
    :   Error message if the request failed

    `h: Optional[float]`
    :   High price

    `l: Optional[float]`
    :   Low price

    `lp: Optional[float]`
    :   LTP

    `ltt: Optional[str]`
    :   Last trade time

    `pc: Optional[float]`
    :   Percentage change

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The get content list success or failure status

    `tsym: Optional[str]`
    :   Trading symbol

    `v: Optional[float]`
    :   Volume