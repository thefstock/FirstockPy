
"""
Request and response models for span calculator request
"""
from typing import List, Optional
from pydantic import BaseModel
from datetime import date, datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder
from ....utils.encoders import build_dumber, date_encoder

__all__ = ['SpanCalculatorRequestModel', 'SpanCalculatorResponseModel', 'SpanCalculatorPos']

class SpanCalculatorPos(BaseModel):
  """
  Each object in pos of SpanCalculatorRequestModel
  """
  exch: Optional[str]
  """Exchange"""
  instname: Optional[str] 
  """Instrument name"""
  symname: Optional[str]
  """Symbol name"""
  expd: Optional[date]
  """expiry date"""
  optt: Optional[str]
  """Option Type"""
  strprc: Optional[float]
  """Strike price"""
  buyqty: Optional[float]
  """Buy Open Quantity"""
  sellqty: Optional[float]
  """Sell Open Quantity"""
  netqty: Optional[float]
  """Net traded quantity"""
  class Config:
    """model configuration"""
    json_dumps = build_dumber({
      "expd": date_encoder('%Y-%m-%d')
    })


class SpanCalculatorRequestModel(BaseModel):
  """
  The request model for span calculator endpoint
  """
  actid: str
  """Any Account id, preferably actual account id if sending from post login screen"""
  pos: List[SpanCalculatorPos]
  """Array of SpanCalculatorPos"""

class SpanCalculatorResponseModel(BaseModel):
  """
  The response model for span calculator endpoint
  """
  stat: ResponseStatus
  """The span calculator success or failure status"""
  request_time: Optional[datetime]
  """It will be present only on successful response."""
  span: Optional[str]
  """Span value"""
  expo: Optional[str]
  """Exposure margin"""
  span_trade: Optional[str]
  """Span value ignoring input fields buyqty, sellqty"""
  expo_trade: Optional[str]
  """Exposure margin ignoring input fields buyqty, sellqty"""
  emsg: Optional[str]
  """Error message if the request failed"""

  class Config:
    """model configuration"""
    json_loads = build_loader({
      "request_time": datetime_decoder()
    })
