"""
Request and Response schema for client_details request
"""

from py_client.common.models import BankDetails, DpAccountNumber
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder, timestamp_decoder

__all__ = ['ClientDetailsRequestModel', 'ClientDetailsResponseModel']

class ClientDetailsRequestModel(BaseModel):
  """
  The request model for client details endpoint
  """
  uid: str
  """The user id of the login user"""
  actid: str
  """Login users account ID"""
  brkname: str
  """Login users broker ID"""

class ClientDetailsResponseModel(BaseModel):
  """
  The response model for client details endpoint
  """
  stat: ResponseStatus
  """The logout success or failure status"""
  actid: Optional[str]
  """Login users account ID"""
  creatdte: Optional[datetime]
  """Creation date"""
  creattme: Optional[datetime]
  """Creation time"""
  m_num: Optional[str]
  """Mobile number"""
  email: Optional[EmailStr]
  """Email Id"""
  pan: Optional[str]
  """The PAN of user"""
  addr: Optional[str]
  """Address"""
  addroffice: Optional[str]
  """Office address"""
  addrcity: Optional[str]
  """City"""
  addrstate: Optional[str]
  """State"""
  bankdetails: Optional[List[BankDetails]]
  """List of bank details"""
  dp_acct_num: Optional[List[DpAccountNumber]]
  """List of bank"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder(),
      "creatdte": timestamp_decoder(),
      "creattme": timestamp_decoder()
    })