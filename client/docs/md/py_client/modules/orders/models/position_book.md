Module py_client.modules.orders.models.position_book
====================================================
Request and Response model for position book request

Classes
-------

`PositionBookRequestModel(**data: Any)`
:   The request model for position book  request
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `uid: str`
    :   Logged in User Id

    `actid: str`
    :   Account Id of logged in user

`PositionBookResponseModel(**data: Any)`
:   The response model for position book endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `stat: py_client.common.enums.ResponseStatus`
    :   The position book success or failure status

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `exch: Optional[str]`
    :   Exchange Segment

    `tsym: Optional[str]`
    :   Trading symbol / contract on which order is placed.

    `token: Optional[str]`
    :   Token

    `uid: Optional[str]`
    :   User Id

    `actid: Optional[str]`
    :   Account Id

    `prd: Optional[str]`
    :   Display product alias name, using prarr returned in user details.

    `netqty: Optional[str]`
    :   Net Position quantity

    `netavgprc: Optional[str]`
    :   Net position average price

    `daybuyqty: Optional[str]`
    :   Day Buy Quantity

    `daysellqty: Optional[str]`
    :   Day Sell Quantity

    `daybuyavgprc: Optional[str]`
    :   Day Buy average price

    `daysellavgprc: Optional[str]`
    :   Day buy average price

    `daybuyamt: Optional[str]`
    :   Day Buy Amount

    `daysellamt: Optional[str]`
    :   Day Sell Amount

    `cfbuyqty: Optional[str]`
    :   Carry Forward Buy Quantity

    `cforgavgprc: Optional[str]`
    :   Original Avg Price

    `cfsellqty: Optional[str]`
    :   Carry Forward Sell Quantity

    `cfbuyavgprc: Optional[str]`
    :   Carry Forward Buy average price

    `cfsellavgprc: Optional[str]`
    :   Carry Forward Buy average price

    `cfbuyamt: Optional[str]`
    :   Carry Forward Buy Amount

    `cfsellamt: Optional[str]`
    :   Carry Forward Sell Amount

    `lp: Optional[str]`
    :   LTP

    `rpnl: Optional[str]`
    :   RealizedPNL

    `urmtom: Optional[str]`
    :   UnrealizedMTOM. 
        (Can be recalculated in LTP update := netqty * (lp from web socket - netavgprc) * prcftr bep Break even price

    `openbuyqty: Optional[str]`
    :

    `opensellqty: Optional[str]`
    :

    `openbuyamt: Optional[str]`
    :

    `opensellamt: Optional[str]`
    :

    `openbuyavgprc: Optional[str]`
    :

    `opensellavgprc: Optional[str]`
    :

    `mult: Optional[str]`
    :

    `pp: Optional[str]`
    :   Price precision

    `ti: Optional[str]`
    :   Tick size

    `ls: Optional[str]`
    :   Lot size

    `prcftr: Optional[str]`
    :   gn*pn/(gd*pd)

    `emsg: Optional[str]`
    :   Error message if the request failed

    `Config`
    :   model configuration