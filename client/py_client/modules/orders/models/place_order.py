"""
Request and Response model for place order request
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import PriceType, ResponseStatus, RetentionType, TransactionType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['PlaceOrderRequestModel', 'PlaceOrderResponseModel']

class PlaceOrderRequestModel(BaseModel):
  """
  The request model for place order request
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
  dscqty: Optional[str]
  """Disclosed quantity (Max 10% for NSE, and 50% for MCX)"""
  prd: str
  """C / M / H Product name (Select from ‘prarr’ Array provided in User Details response, and if same is allowed for selected, exchange. Show product display name, for user to select, and send corresponding prd in API call)"""
  trantype: TransactionType
  """B / S B -> BUY, S -> SELL"""
  prctyp: PriceType
  """LMT / MKT / SLLMT / SL-MKT / DS / 2L / 3L"""
  ret: RetentionType
  """DAY / EOS / IOC Retention type (Show options as per allowed exchanges) remarks Any tag by user to mark order."""
  ordersource: Optional[str]
  """MOB / WEB / TT Used to generate exchange info fields."""
  bpprc: Optional[str]
  """Book Profit Price applicable only if product is selected as B (Bracket order )"""
  blprc: Optional[str]
  """Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order )"""
  trailprc: Optional[str]
  """Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order )"""
  amo: Optional[str]
  """Yes , If not sent, of Not “Yes”, will be treated as Regular order."""
  tsym2: Optional[str]
  """Trading symbol of second leg, mandatory for price type 2L and 3L (use url encoding to avoid special char error for symbols like M&M)"""
  trantype2: Optional[TransactionType]
  """Transaction type of second leg, mandatory for price type 2L and 3L"""
  qty2: Optional[str]
  """Quantity for second leg, mandatory for price type 2L and 3L"""
  prc2: Optional[str]
  """Price for second leg, mandatory for price type 2L and 3L"""
  tsym3: Optional[str]
  """Trading symbol of third leg, mandatory for price type 3L (use url encoding to avoid special char error for symbols like M&M)"""
  trantype3: Optional[TransactionType]
  """Transaction type of third leg, mandatory for price type 3L"""
  qty3: Optional[str]
  """Quantity for third leg, mandatory for price type 3L"""
  prc3: Optional[str]
  """Price for third leg, mandatory for price type 3L"""

class PlaceOrderResponseModel(BaseModel):
  """
  The response model for place order endpoint
  """
  stat: ResponseStatus
  """The place order success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  norenordno: Optional[str]
  """It will be present only on successful Order placement to OMS."""
  emsg: Optional[str]
  """Error message if the request failed"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })