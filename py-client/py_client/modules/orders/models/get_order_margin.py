"""
Request and Response model for get order margin request
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import PriceType, ResponseStatus, TransactionType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetOrderMarginRequestModel', 'GetOrderMarginResponseModel']

class GetOrderMarginRequestModel(BaseModel):
  """
  The request model for get order margin  request
  """
  uid: str
  """Logged in User Id"""
  actid: str
  """Login users account ID"""
  exch: str
  """Exchange (Select from ‘exarr’ Array provided in User Details response)"""
  tsym: str
  """Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M)"""
  qty: str
  """Order Quantity"""
  prc: str
  """Order Price"""
  trgprc: Optional[str]
  """Only to be sent in case of SL / SL-M order."""
  prd: str
  """C / M / H Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call)"""
  trantype: TransactionType
  """BUY or SELL"""
  prctyp: PriceType
  """LMT / MKT / SLLMT / SL-MKT / DS / 2L / 3L"""
  blprc: Optional[str]
  """Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order )"""
  rorgqty: Optional[str]
  """Optional field. Application only for modify order, open order quantity"""
  fillshares: Optional[str]
  """Optional field. Application only for modify order, quantity already filled"""
  rorgprc: Optional[str]
  """Optional field. Application only for modify order, open order price"""
  orgtrgprc: Optional[str]
  """Optional field. Application only for modify order, open order trigger price"""
  norenordno: Optional[str]
  """Optional field. Application only for H or B order modification"""
  snonum: Optional[str]
  """Optional field. Application only for H or B order modification"""

class GetOrderMarginResponseModel(BaseModel):
  """
  The response model for get order margin endpoint
  """
  stat: ResponseStatus
  """The get order margin success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  remarks: Optional[str]
  """This field will be available only on success."""
  cash: Optional[str]
  """Total credits available for order"""
  marginused: Optional[str]
  """Total margin used."""
  emsg: Optional[str]
  """Error message if the request failed"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })