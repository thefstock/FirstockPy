"""
Request and Response model for modify order request
"""

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import PriceType, ResponseStatus, RetentionType
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['ModifyOrderRequestModel', 'ModifyOrderResponseModel']

class ModifyOrderRequestModel(BaseModel):
  """
  The request model for modify order  request
  """
  uid: str
  """Logged in User Id"""
  exch: str
  """Exchange"""
  norenordno: str
  """Noren order number, which needs to be modified"""
  tsym: str
  """Unique id of contract on which order to be placed. (use url encoding to avoid special char error for symbols like M&M)"""
  qty: Optional[str]
  """Modified / New Quantity"""
  prc: Optional[str]
  """Modified / New price"""
  trgprc: Optional[str]
  """New trigger price in case of SL-MKT or SL-LMT"""
  prctyp: PriceType
  """LMT / MKT / SLLMT / SL-MKT / DS / 2L / 3L"""
  ret: RetentionType
  """New Retention type of the order."""
  bpprc: Optional[str]
  """Book Profit Price applicable only if product is selected as B (Bracket order )"""
  blprc: Optional[str]
  """Book loss Price applicable only if product is selected as H and B (High Leverage and Bracket order )"""
  trailprc: Optional[str]
  """Trailing Price applicable only if product is selected as H and B (High Leverage and Bracket order )"""

class ModifyOrderResponseModel(BaseModel):
  """
  The response model for modify order endpoint
  """
  stat: ResponseStatus
  """The modify order success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  result: Optional[str]
  """Noren Order number of the order modified."""
  emsg: Optional[str]
  """Error message if the request failed"""
  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })