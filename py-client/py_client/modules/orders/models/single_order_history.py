"""
Request and Response model for single order history request
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import PriceType, ResponseStatus, RetentionType, TransactionType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['SingleOrderHistoryRequestModel', 'SingleOrderHistoryResponseModel']

class SingleOrderHistoryRequestModel(BaseModel):
  """
  The request model for single order history  request
  """
  uid: str
  """Logged in User Id"""
  norenord: str
  """Noren Order Number"""

class SingleOrderHistoryResponseModel(BaseModel):
  """
  The response model for single order history endpoint
  """
  stat: ResponseStatus
  """The single order history success or failure status"""
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
  status: Optional[str]
  """Order status"""
  rpt: Optional[str]
  """Report Type (fill/complete etc)"""
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
  cancelqty: Optional[str]
  """Canceled quantity for order which is in status cancelled."""
  remarks: Optional[str]
  """Any message Entered during order entry."""
  dscqty: Optional[str]
  """Order disclosed quantity."""
  trgprc: Optional[str]
  """Order trigger price"""
  ret: Optional[RetentionType]
  """DAY / IOC / EOS Order validity"""
  uid: Optional[str]
  """User Id"""
  actid: Optional[str]
  """Account Id"""
  bpprc: Optional[str]
  """Book Profit Price applicable only if product is selected as B (Bracket order )"""
  blprc: Optional[str]
  """Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order )"""
  trailprc: Optional[str]
  """Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order )"""
  amo: Optional[str]
  """Yes / No"""
  pp: Optional[str]
  """Price precision"""
  ti: Optional[str]
  """Tick size"""
  ls: Optional[str]
  """Lot size"""
  token: Optional[str]
  """Contract Token"""
  orddttm: Optional[str]
  "orddttm"
  ordenttm: Optional[str]
  """ordenttm"""
  extm: Optional[str]
  """extm"""
  emsg: Optional[str]
  """Error message if the request failed"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })