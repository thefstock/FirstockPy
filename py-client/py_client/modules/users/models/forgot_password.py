"""
Request and response models for forgot password
"""
from typing import Optional, Union
from pydantic import BaseModel, validator
from datetime import date, datetime

from ....utils.encoders import date_encoder
from ....utils.decoders import build_loader, datetime_decoder
from ....common.enums import ResponseStatus

__all__ = ['ForgotPasswordRequestModel', 'ForgotPasswordResponseModel']

class ForgotPasswordRequestModel(BaseModel):
  """
  The request model for forgot password endpoint
  """
  uid: str
  """User Id"""
  pan: str
  """PAN of the user"""
  dob: date
  """Date of birth"""

  class Config:
    """model configuration"""
    json_encoders = {
      date: date_encoder()
    }

class ForgotPasswordResponseModel(BaseModel):
  """
  The response model for forgot password endpoint
  """
  stat: ResponseStatus
  """Password reset is Success Or failure status"""
  request_time: datetime
  """Response received time"""
  emsg: Optional[str]
  """Error message if the forgot password failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })