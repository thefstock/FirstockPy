"""
Request and response models for fetching user details
"""
from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

from ....common.enums import ResponseStatus
from ....common.models import Product
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['UserDetailsRequestModel', 'UserDetailsResponseModel']

class UserDetailsRequestModel(BaseModel):
  """
  The request model for user details endpoint
  """
  uid: str
  """The user id of the login user"""

class UserDetailsResponseModel(BaseModel):
  """
  The response model for user details endpoint
  """
  stat: ResponseStatus
  """The logout success or failure status"""
  exarr: Optional[List[str]]
  """List of strings with enabled exchange names"""
  orarr: Optional[List[str]]
  """List of strings with enabled price types for user"""
  prarr: Optional[List[Product]]
  """List of Product Obj with enabled products, as defined below."""
  brkname: Optional[str]
  """Broker Id"""
  brnchid: Optional[str]
  """Branch Id"""
  email: Optional[EmailStr]
  """Email Id"""
  actid: Optional[str]
  """Account Id"""
  m_num: Optional[str]
  """Mobile Number"""
  u_prev: Optional[str]
  """Always it will be an INVESTOR, other types of user not allowed to login using this API."""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })