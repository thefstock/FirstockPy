
"""
Request and response models for get index list request
"""
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....common.models import IndexTokenPair
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['GetIndexListRequestModel', 'GetIndexListResponseModel']

class GetIndexListRequestModel(BaseModel):
  """
  The request model for get index list endpoint
  """
  uid: str
  """The user id of the login user"""
  exch: str
  """Exchange"""

class GetIndexListResponseModel(BaseModel):
  """
  The response model for get index list endpoint
  """
  stat: ResponseStatus
  """The get index list success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  values: Optional[List[IndexTokenPair]]
  """Array Of index token pair."""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
