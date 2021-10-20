"""
Request and Response model for trade book request
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import PriceType, ResponseStatus, RetentionType, TransactionType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['TradeBookRequestModel', 'TradeBookResponseModel']

class TradeBookRequestModel(BaseModel):
  """
  The request model for trade book  request
  """
  uid: str
  """Logged in User Id"""
  actid: str
  """Account Id of logged in user"""

class TradeBookResponseModel(BaseModel):
  """
  The response model for trade book endpoint
  """
  stat: ResponseStatus
  """The trade book success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  exch: Optional[str]
  """Exchange Segment"""
  tsym: Optional[str]
  """Trading symbol / contract on which order is placed."""
  norenordno: Optional[str]
  """Noren Order Number"""
  prc: Optional[str]
  """Order Price"""
  qty: Optional[str]
  """Order Quantity"""
  prd: Optional[str]
  """Display product alias name, using prarr returned in user details."""
  trantype: Optional[TransactionType]
  """B / S Transaction type of the order"""
  prctyp: Optional[PriceType]
  """LMT / MKT Price type"""
  fillshares: Optional[str]
  """Total Traded Quantity of this order"""
  avgprc: Optional[str]
  """Average trade price of total traded quantity"""
  rejreason: Optional[str]
  """If order is rejected, reason in text form"""
  exchordid: Optional[str]
  """Exchange Order Number"""
  ret: Optional[RetentionType]
  """DAY / IOC / EOS Order validity"""
  uid: Optional[str]
  """User Id"""
  actid: Optional[str]
  """Account Id"""
  pp: Optional[str]
  """Price precision"""
  ti: Optional[str]
  """Tick size"""
  ls: Optional[str]
  """Lot size"""
  cstFrm: Optional[str]
  """Custom Firm"""
  fltm: Optional[str]
  """Fill Time"""
  flid: Optional[str]
  """Fill ID"""
  flqty: Optional[str]
  """Fill Qty"""
  flprc: Optional[str]
  """Fill Price"""
  ordersource: Optional[str]
  """Order Source"""
  token: Optional[str]
  """Token"""
  emsg: Optional[str]
  """Error message if the request failed"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })