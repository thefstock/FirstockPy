
"""
Request and response models for modify gtt order request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus, AlertValidity, TransactionType, PriceType, RetentionType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['ModifyGttOrderRequestModel', 'ModifyGttOrderResponseModel']

class ModifyGttOrderRequestModel(BaseModel):
  """
  The request model for modify gtt order endpoint
  """
  uid: str
  """The user id of the login user"""
  tsym: str
  """Trading symbol"""
  exch: str
  """Exchange Segment"""
  ai_t: str
  """Alert Type. should be original type can't be modified"""
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

class ModifyGttOrderResponseModel(BaseModel):
  """
  The response model for modify gtt order endpoint
  """
  stat: ResponseStatus
  """The modify gtt order success or failure status"""
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
