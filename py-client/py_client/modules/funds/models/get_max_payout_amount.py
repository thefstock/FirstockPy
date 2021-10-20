
"""
Request and response models for get max payout amount request
"""
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetMaxPayoutAmountRequestModel', 'GetMaxPayoutAmountResponseModel']

class GetMaxPayoutAmountRequestModel(BaseModel):
  """
  The request model for get max payout amount endpoint
  """
  uid: str
  """The user id of the login user"""
  actid: str
  """The account id"""

class GetMaxPayoutAmountResponseModel(BaseModel):
  """
  The response model for get max payout amount endpoint
  """
  stat: ResponseStatus
  """The get max payout amount success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  actid: Optional[str]
  """Account Id"""
  payout: Optional[float]
  """Maximum payout amount"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
