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

    `actid: str`
    :   Account Id of logged in user

    `uid: str`
    :   Logged in User Id

`PositionBookResponseModel(**data: Any)`
:   The response model for position book endpoint
    
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

    `cfbuyamt: Optional[str]`
    :   Carry Forward Buy Amount

    `cfbuyavgprc: Optional[str]`
    :   Carry Forward Buy average price

    `cfbuyqty: Optional[str]`
    :   Carry Forward Buy Quantity

    `cforgavgprc: Optional[str]`
    :   Original Avg Price

    `cfsellamt: Optional[str]`
    :   Carry Forward Sell Amount

    `cfsellavgprc: Optional[str]`
    :   Carry Forward Buy average price

    `cfsellqty: Optional[str]`
    :   Carry Forward Sell Quantity

    `daybuyamt: Optional[str]`
    :   Day Buy Amount

    `daybuyavgprc: Optional[str]`
    :   Day Buy average price

    `daybuyqty: Optional[str]`
    :   Day Buy Quantity

    `daysellamt: Optional[str]`
    :   Day Sell Amount

    `daysellavgprc: Optional[str]`
    :   Day buy average price

    `daysellqty: Optional[str]`
    :   Day Sell Quantity

    `emsg: Optional[str]`
    :   Error message if the request failed

    `exch: Optional[str]`
    :   Exchange Segment

    `lp: Optional[str]`
    :   LTP

    `ls: Optional[str]`
    :   Lot size

    `mult: Optional[str]`
    :

    `netavgprc: Optional[str]`
    :   Net position average price

    `netqty: Optional[str]`
    :   Net Position quantity

    `openbuyamt: Optional[str]`
    :

    `openbuyavgprc: Optional[str]`
    :

    `openbuyqty: Optional[str]`
    :

    `opensellamt: Optional[str]`
    :

    `opensellavgprc: Optional[str]`
    :

    `opensellqty: Optional[str]`
    :

    `pp: Optional[str]`
    :   Price precision

    `prcftr: Optional[str]`
    :   gn*pn/(gd*pd)

    `prd: Optional[str]`
    :   Display product alias name, using prarr returned in user details.

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `rpnl: Optional[str]`
    :   RealizedPNL

    `stat: py_client.common.enums.ResponseStatus`
    :   The position book success or failure status

    `ti: Optional[str]`
    :   Tick size

    `token: Optional[str]`
    :   Token

    `tsym: Optional[str]`
    :   Trading symbol / contract on which order is placed.

    `uid: Optional[str]`
    :   User Id

    `urmtom: Optional[str]`
    :   UnrealizedMTOM. 
        (Can be recalculated in LTP update := netqty * (lp from web socket - netavgprc) * prcftr bep Break even price