"""
Request and Response model for multileg order book request
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import PriceType, ResponseStatus, RetentionType, TransactionType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['MultilegOrderBookRequestModel', 'MultilegOrderBookResponseModel']

class MultilegOrderBookRequestModel(BaseModel):
  """
  The request model for multileg order book  request
  """
  uid: str
  """Logged in User Id"""
  prd: Optional[str]
  """The product name"""

class MultilegOrderBookResponseModel(BaseModel):
  """
  The response model for multileg order book endpoint
  """
  stat: ResponseStatus
  """The multileg order book success or failure status"""
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
  tsym2: Optional[str]
  """Trading symbol of second leg, mandatory for price type 2L and 3L"""
  trantype2: Optional[TransactionType]
  """Transaction type of second leg, mandatory for price type 2L and 3L"""
  qty2: Optional[str]
  """Quantity for second leg, mandatory for price type 2L and 3L"""
  prc2: Optional[str]
  """Price for second leg, mandatory for price type 2L and 3L"""
  tsym3: Optional[str]
  """Trading symbol of third leg, mandatory for price type 3L"""
  trantype3: Optional[TransactionType]
  """Transaction type of third leg, mandatory for price type 3L"""
  qty3: Optional[str]
  """Quantity for third leg, mandatory for price type 3L"""
  prc3: Optional[str]
  """Price for third leg, mandatory for price type 3L"""
  fillshares2: Optional[str]
  """Total Traded Quantity of 2nd Leg"""
  avgprc2: Optional[str]
  """Average trade price of total traded quantity for 2nd leg"""
  fillshares3: Optional[str]
  """Total Traded Quantity of 3rd Leg"""
  avgprc3: Optional[str]
  """Average trade price of total traded quantity for 3rd leg"""
  emsg: Optional[str]
  """Error message if the request failed"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })