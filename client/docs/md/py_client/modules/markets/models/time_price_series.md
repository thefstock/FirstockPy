Module py_client.modules.markets.models.time_price_series
=========================================================
Request and response models for time price series request

Classes
-------

`TimePriceSeriesRequestModel(**data: Any)`
:   The request model for time price series endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `et: datetime.datetime`
    :   End Time

    `exch: str`
    :   Exchange

    `st: datetime.datetime`
    :   Start time

    `token: str`
    :   Token

    `uid: str`
    :   The user id of the login user

`TimePriceSeriesResponseModel(**data: Any)`
:   The response model for time price series endpoint
    
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

    `intc: Optional[str]`
    :   Interval close

    `inth: Optional[str]`
    :   Interval high

    `intl: Optional[str]`
    :   Interval low

    `into: Optional[str]`
    :   Interval open

    `intoi: Optional[str]`
    :   Interval io change

    `intv: Optional[str]`
    :   Interval volume

    `intvwap: Optional[str]`
    :   Interval vwap

    `oi: Optional[str]`
    :   oi

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The time price series success or failure status

    `time: Optional[datetime.datetime]`
    :   DD/MM/CCYY hh:mm:ss

    `v: Optional[str]`
    :   volume