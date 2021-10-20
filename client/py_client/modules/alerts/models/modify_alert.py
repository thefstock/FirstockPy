
"""
Request and response models for modify alert request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus, AlertValidity
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['ModifyAlertRequestModel', 'ModifyAlertResponseModel']

class ModifyAlertRequestModel(BaseModel):
  """
  The request model for modify alert endpoint
  """
  uid: str
  """The user id of the login user"""
  al_id: str
  """The id of the alert to modify"""
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

class ModifyAlertResponseModel(BaseModel):
  """
  The response model for modify alert endpoint
  """
  stat: ResponseStatus
  """The modify alert success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  al_id: str
  """The modified alert id"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
