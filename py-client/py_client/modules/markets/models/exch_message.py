
"""
Request and response models for exch message request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['ExchMessageRequestModel', 'ExchMessageResponseModel']

class ExchMessageRequestModel(BaseModel):
  """
  The request model for exch message endpoint
  """
  uid: str
  """The user id of the login user"""
  exch: Optional[str]
  """Exchange"""

class ExchMessageResponseModel(BaseModel):
  """
  The response model for exch message endpoint
  """
  stat: ResponseStatus
  """The exch message success or failure status"""
  request_time: Optional[datetime]
  """Response recieved time"""
  exchmsg: Optional[str]
  """It will be present only on a successful response"""
  exchtm: Optional[datetime]
  """Exchange Time"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder(),
      "exchtm": datetime_decoder()
    })
