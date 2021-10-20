
"""
Request and response models for get unsettled trading date request
"""
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....common.models import TradeDate
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetUnsettledTradingDateRequestModel', 'GetUnsettledTradingDateResponseModel']

class GetUnsettledTradingDateRequestModel(BaseModel):
  """
  The request model for get unsettled trading date endpoint
  """
  uid: str
  """The user id of the login user"""

class GetUnsettledTradingDateResponseModel(BaseModel):
  """
  The response model for get unsettled trading date endpoint
  """
  stat: ResponseStatus
  """The get unsettled trading date success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  trd_date: Optional[List[TradeDate]]
  """The list of trade date items"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
