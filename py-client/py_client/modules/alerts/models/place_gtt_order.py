
"""
Request and response models for place gtt order request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import AlertValidity, PriceType, ResponseStatus, RetentionType, TransactionType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['PlaceGttOrderRequestModel', 'PlaceGttOrderResponseModel']

class PlaceGttOrderRequestModel(BaseModel):
  """
  The request model for place gtt order endpoint
  """
  uid: str
  """The user id of the login user"""
  tsym: str
  """Trading symbol"""
  exch: str
  """Exchange Segment"""
  ai_t: str
  """Alert Type"""
  validity: AlertValidity
  """DAY or GTT Validity"""
  remarks: str
  """Any message Entered during order entry."""
  d: str
  """Data to be compared with LTP"""
  trantype: TransactionType
  """Transaction type"""
  prctyp: PriceType
  """Price type"""
  prd: str
  """The product name"""
  ret: RetentionType
  """Retention type"""
  actid: str
  """Login user account id"""
  prc: str
  """Order price"""
  qty: str
  """Order quantity"""
  dscqty: Optional[str]
  """Disclosed quantity (Max 10% for NSE, and 50% for MCX)"""

class PlaceGttOrderResponseModel(BaseModel):
  """
  The response model for place gtt order endpoint
  """
  stat: ResponseStatus
  """The place gtt order success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  al_id: Optional[str]
  """Alert Id"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
