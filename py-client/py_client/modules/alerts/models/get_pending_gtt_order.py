
"""
Request and response models for get pending gtt order request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import AlertValidity, PriceType, ResponseStatus, RetentionType, TransactionType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetPendingGttOrderRequestModel', 'GetPendingGttOrderResponseModel']

class GetPendingGttOrderRequestModel(BaseModel):
  """
  The request model for get pending gtt order endpoint
  """
  uid: str
  """The user id of the login user"""

class GetPendingGttOrderResponseModel(BaseModel):
  """
  The response model for get pending gtt order endpoint
  """
  stat: ResponseStatus
  """The get pending gtt order success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  tsym: Optional[str]
  """Trading symbol"""
  exch: Optional[str]
  """Exchange Segment"""
  ai_t: Optional[str]
  """Alert Type"""
  al_id: Optional[str]
  """Alert id"""
  validity: Optional[AlertValidity]
  """DAY or GTT Validity"""
  remarks: Optional[str]
  """Any message Entered during order entry."""
  d: Optional[str]
  """Data to be compared with LTP"""
  trantype: Optional[TransactionType]
  """Transaction type"""
  prctyp: Optional[PriceType]
  """Price type"""
  prd: Optional[str]
  """The product name"""
  ret: RetentionType
  """Retention type"""
  actid: Optional[str]
  """Login user account id"""
  prc: Optional[str]
  """Order price"""
  qty: Optional[str]
  """Order quantity"""
  dscqty: Optional[str]
  """Disclosed quantity (Max 10% for NSE, and 50% for MCX)"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
