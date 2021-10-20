
"""
Request and response models for top list names request
"""
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....common.models import BasketCriteriaPair
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['TopListNamesRequestModel', 'TopListNamesResponseModel']

class TopListNamesRequestModel(BaseModel):
  """
  The request model for top list names endpoint
  """
  uid: str
  """The user id of the login user"""
  exch: str
  """Exchange"""

class TopListNamesResponseModel(BaseModel):
  """
  The response model for top list names endpoint
  """
  stat: ResponseStatus
  """The top list names success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  values: Optional[List[BasketCriteriaPair]]
  """Array of Basket, Criteria pair"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
