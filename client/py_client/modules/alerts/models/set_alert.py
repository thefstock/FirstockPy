
"""
Request and response models for set alert request
"""
from typing import Optional, Union
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import AlertType, AlertValidity, ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['SetAlertRequestModel', 'SetAlertResponseModel']

class SetAlertRequestModel(BaseModel):
  """
  The request model for set alert endpoint
  """
  uid: str
  """The user id of the login user"""
  tsym: str
  """Trading symbol"""
  exch: str
  """Exchange Segment"""
  ai_t: AlertType
  """Alert Type"""
  validity: AlertValidity
  """DAY or GTT Validity"""
  remarks: str
  """Any message Entered during order entry."""
  d: Optional[str]
  """Data to be compared with LTP"""

class SetAlertResponseModel(BaseModel):
  """
  The response model for set alert endpoint
  """
  stat: Union[ResponseStatus, str]
  """The set alert success or failure status"""
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
