Module py_client.modules.markets.models.span_calculator
=======================================================
Request and response models for span calculator request

Classes
-------

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

    `stat: py_client.common.enums.ResponseStatus`
    :   The span calculator success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `span: Optional[str]`
    :   Span value

    `expo: Optional[str]`
    :   Exposure margin

    `span_trade: Optional[str]`
    :   Span value ignoring input fields buyqty, sellqty

    `expo_trade: Optional[str]`
    :   Exposure margin ignoring input fields buyqty, sellqty

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration

`SpanCalculatorPos(**data: Any)`
:   Each object in pos of SpanCalculatorRequestModel
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `exch: Optional[str]`
    :   Exchange

    `instname: Optional[str]`
    :   Instrument name

    `symname: Optional[str]`
    :   Symbol name

    `expd: Optional[datetime.date]`
    :   expiry date

    `optt: Optional[str]`
    :   Option Type

    `strprc: Optional[float]`
    :   Strike price

    `buyqty: Optional[float]`
    :   Buy Open Quantity

    `sellqty: Optional[float]`
    :   Sell Open Quantity

    `netqty: Optional[float]`
    :   Net traded quantity

    `Config`
    :   model configuration