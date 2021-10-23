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

    `uid: str`
    :   The user id of the login user

    `exch: str`
    :   Exchange

    `token: str`
    :   Token

    `st: datetime.datetime`
    :   Start time

    `et: datetime.datetime`
    :   End Time

    `Config`
    :   model configuration

`TimePriceSeriesResponseModel(**data: Any)`
:   The response model for time price series endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The time price series success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `time: Optional[datetime.datetime]`
    :   DD/MM/CCYY hh:mm:ss

    `into: Optional[str]`
    :   Interval open

    `inth: Optional[str]`
    :   Interval high

    `intl: Optional[str]`
    :   Interval low

    `intc: Optional[str]`
    :   Interval close

    `intvwap: Optional[str]`
    :   Interval vwap

    `intv: Optional[str]`
    :   Interval volume

    `v: Optional[str]`
    :   volume

    `intoi: Optional[str]`
    :   Interval io change

    `oi: Optional[str]`
    :   oi

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration