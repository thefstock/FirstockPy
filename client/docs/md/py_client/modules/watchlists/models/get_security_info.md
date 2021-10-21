Module py_client.modules.watchlists.models.get_security_info
============================================================
The request and response models for get security info request

Classes
-------

`GetSecurityInfoRequestModel(**data: Any)`
:   The request model for get security infoendpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `exch: Optional[str]`
    :   Exchange

    `token: Optional[str]`
    :   Contract Token

    `uid: str`
    :   The user id of the login user

`GetSecurityInfoResponseModel(**data: Any)`
:   The response model for get security info endpoint
    
    Create a new model by parsing and validating input data from keyword arguments.
    
    Raises ValidationError if the input data cannot be parsed to form a valid model.

    ### Ancestors (in MRO)

    * pydantic.main.BaseModel
    * pydantic.utils.Representation

    ### Class variables

    `Config`
    :   model configuration

    `addbmrg: Optional[str]`
    :   Additional Long Margin

    `addsmrg: Optional[str]`
    :   Additional Short Margin

    `cname: Optional[str]`
    :   Company Name

    `delmrg: Optional[str]`
    :   Delivery Margin

    `delunt: Optional[str]`
    :   Delivery Units

    `elmbmrg: Optional[str]`
    :   Elm Buy Margin

    `elmmrg: Optional[str]`
    :   Elm Margin

    `elmsmrg: Optional[str]`
    :   Elm Sell Margin

    `emsg: Optional[str]`
    :   Error message if the request failed

    `exch: Optional[str]`
    :   Exchange

    `exd: Optional[str]`
    :   Expiry Date

    `exeendd: Optional[str]`
    :   Exercise End Date

    `exestrd: Optional[str]`
    :   Exercise Start Date

    `expmrg: Optional[str]`
    :   Exposure Margin

    `frzqty: Optional[float]`
    :   Freeze Qty

    `gp_nd: Optional[str]`
    :   gn/gd * pn/pd

    `gsmind: Optional[str]`
    :   scripupdate Gsm Ind

    `instname: Optional[str]`
    :   Intrument Name

    `isin: Optional[str]`
    :   ISIN

    `ls: Optional[float]`
    :   Lot Size

    `mult: Optional[float]`
    :   Multiplier

    `optt: Optional[str]`
    :   Option Type

    `pp: Optional[float]`
    :   Price precision

    `prcftr_d: Optional[str]`
    :   ((GN / GD) * (PN/PD))

    `prcqqty: Optional[float]`
    :   Price Quote Qty

    `prcunt: Optional[float]`
    :   Price Units

    `request_time: Optional[datetime.datetime]`
    :   It will be present only on successful response.

    `seg: Optional[str]`
    :   Segment

    `splbmrg: Optional[str]`
    :   Special Long Margin

    `splsmrg: Optional[str]`
    :   Special Short Margin

    `stat: py_client.common.enums.ResponseStatus`
    :   The get security info success or failure status

    `strprc: Optional[str]`
    :   Strike Price

    `symnam: Optional[str]`
    :   Symbol Name

    `tenendd: Optional[str]`
    :   Tender End Eate

    `tenmrg: Optional[str]`
    :   Tender Margin

    `tenstrd: Optional[str]`
    :   Tender Start Date

    `ti: Optional[float]`
    :   Tick Size

    `token: Optional[str]`
    :   Contract Token

    `trdunt: Optional[str]`
    :   Trade Units

    `tsym: Optional[str]`
    :   Trading Symbol

    `varmrg: Optional[str]`
    :   Var Margin