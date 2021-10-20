
"""
Request and response models for top list request
"""
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....common.models import TBContract
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['TopListRequestModel', 'TopListResponseModel']

class TopListRequestModel(BaseModel):
  """
  The request model for top list endpoint
  """
  uid: str
  """The user id of the login user"""
  exch: str 
  """Exchange"""
  tb: str
  """T or B Top or Bottom"""
  bskt: str
  """Basket name"""
  crt: str
  """Criteria"""

class TopListResponseModel(BaseModel):
  """
  The response model for top list endpoint
  """
  stat: ResponseStatus
  """The top list success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  values: Optional[List[TBContract]]
  """Array of top / bottom contracts object"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
