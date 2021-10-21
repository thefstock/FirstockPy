Module py_client.modules.markets.models.span_calculator
=======================================================
Request and response models for span calculator request

Classes
-------

`SpanCalculatorPos(**data: Any)`
:   Each object in pos of SpanCalculatorRequestModel
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `buyqty: Optional[float]`
    :   Buy Open Quantity

    `exch: Optional[str]`
    :   Exchange

    `expd: Optional[datetime.date]`
    :   expiry date

    `instname: Optional[str]`
    :   Instrument name

    `netqty: Optional[float]`
    :   Net traded quantity

    `optt: Optional[str]`
    :   Option Type

    `sellqty: Optional[float]`
    :   Sell Open Quantity

    `strprc: Optional[float]`
    :   Strike price

    `symname: Optional[str]`
    :   Symbol name

`SpanCalculatorRequestModel(**data: Any)`
:   The request model for span calculator endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `actid: str`
    :   Any Account id, preferably actual account id if sending from post login screen

    `pos: List[py_client.modules.markets.models.span_calculator.SpanCalculatorPos]`
    :   Array of SpanCalculatorPos

`SpanCalculatorResponseModel(**data: Any)`
:   The response model for span calculator endpoint
    
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

    `expo: Optional[str]`
    :   Exposure margin

    `expo_trade: Optional[str]`
    :   Exposure margin ignoring input fields buyqty, sellqty

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `span: Optional[str]`
    :   Span value

    `span_trade: Optional[str]`
    :   Span value ignoring input fields buyqty, sellqty

    `stat: py_client.common.enums.ResponseStatus`
    :   The span calculator success or failure status