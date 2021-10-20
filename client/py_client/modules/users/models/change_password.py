"""
Request and response models for change password
"""

from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from pydantic.types import SecretStr

from ....utils.encoders import password_hash_encoder
from ....utils.decoders import build_loader, datetime_decoder
from ....common.enums import ResponseStatus

__all__ = ['ChangePasswordRequestModel', 'ChangePasswordResponseModel']

class ChangePasswordRequestModel(BaseModel):
  """
  The request model for change password endpoint
  """
  uid: str
  """User Id"""
  oldpwd: SecretStr
  """The old password"""
  pwd: str
  """The new password"""

  class Config:
    """model configuration"""
    json_encoders = {
      SecretStr: password_hash_encoder()
    }

class ChangePasswordResponseModel(BaseModel):
  """
  The response model for change password endpoint
  """
  stat: ResponseStatus
  """Password change success or failure status"""
  request_time: datetime
  """Response recieved time"""
  dmsg: Optional[str]
  """This will be present only in case of success. Number of days to expiry will be present in same."""
  emsg: Optional[str]
  """Error message if password change failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })