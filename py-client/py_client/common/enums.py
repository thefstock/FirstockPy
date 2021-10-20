"""
Commonly used enumerators
"""
from enum import Enum

__all__ = [
  'RequestSourceType',
  'ResponseStatus',
  'RestMethod'
]

class RequestSourceType(str, Enum):
  """
  The source of the request, mobile or web
  """
  MOB = 'MOB'
  WEB = 'WEB'
  API = 'API'

class ResponseStatus(str, Enum):
  """
  The response success or failure status
  """
  OK = 'Ok'
  NOT_OK = 'Not_Ok'

class RestMethod(str, Enum):
  """
  Enumeration for REST methods
  """
  GET = 'get'
  POST = 'post'
  PATCH = 'patch'
  PUT = 'put'
  DELETE = 'delete'
  OPTION = 'option'
  HEAD = 'head'

class PriceType(str, Enum):
  """
  The price type for orders & trades
  """
  LIMIT = 'LMT'
  MARKET = 'MKT'
  STOP_LOSS_LIMIT = 'SL-LMT'
  STOP_LOSS_MARKET = 'SL-MKT'
  DS = 'DS'
  SECOND_LEG = '2L'
  THIRD_LEG = '3L'

class TransactionType(str, Enum):
  """
  The transaction type for orders & trades
  """
  BUY = 'B'
  SELL = 'S'

class RetentionType(str, Enum):
  """
  The retention type for orders
  """
  DAY = 'DAY'
  IOC = 'IOC'
  EOS = 'EOS'

class AlertValidity(str, Enum):
  """
  The alert validity
  """
  DAY = 'DAY'
  GTT = 'GTT'