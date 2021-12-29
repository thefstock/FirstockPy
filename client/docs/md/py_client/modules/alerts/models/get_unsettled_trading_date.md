Module py_client.modules.alerts.models.get_unsettled_trading_date
=================================================================
Request and response models for get unsettled trading date request

Classes
-------

`GetUnsettledTradingDateRequestModel(**data: Any)`
:   The request model for get unsettled trading date endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   The user id of the login user

`GetUnsettledTradingDateResponseModel(**data: Any)`
:   The response model for get unsettled trading date endpoint
    
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

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `stat: py_client.common.enums.ResponseStatus`
    :   The get unsettled trading date success or failure status

    `trd_date: Optional[List[py_client.common.models.TradeDate]]`
    :   The list of trade date items