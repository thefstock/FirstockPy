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

    `uid: str`
    :   The user id of the login user

    `exch: str`
    :   Exchange Name

    `condition_name: str`
    :   condition list

    `basket: Optional[str]`
    :   Basket Name

`GetContentListResponseModel(**data: Any)`
:   The response model for get content list endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The get content list success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `tsym: Optional[str]`
    :   Trading symbol

    `lp: Optional[float]`
    :   LTP

    `c: Optional[float]`
    :   Close price

    `h: Optional[float]`
    :   High price

    `l: Optional[float]`
    :   Low price

    `ap: Optional[float]`
    :   Average trade price

    `v: Optional[float]`
    :   Volume

    `ltt: Optional[str]`
    :   Last trade time

    `pc: Optional[float]`
    :   Percentage change

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration