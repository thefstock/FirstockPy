
"""
Datasource for handling holdings_limits operations
"""
from ...utils.datasources import NorenRestDataSource
from . import endpoints
from .models import *

class HoldingsLimitsDataSource(NorenRestDataSource):
  """
  Datasource for handling holdings_limits operations
  """

  def holdings(self, model: HoldingsRequestModel, key: str = None) -> HoldingsResponseModel:
    """
    Holdings

    Args:
      model (HoldingsRequestModel): The data to be send as HoldingsRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      HoldingsResponseModel: The response as HoldingsResponseModel.
    """
    response_json = self._run_request(model, endpoints.HOLDINGS, key)
    # convert the request to response model
    return HoldingsResponseModel.parse_raw(response_json)

  def limits(self, model: LimitsRequestModel, key: str = None) -> LimitsResponseModel:
    """
    Limits

    Args:
      model (LimitsRequestModel): The data to be send as LimitsRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      LimitsResponseModel: The response as LimitsResponseModel.
    """
    response_json = self._run_request(model, endpoints.LIMITS, key)
    # convert the request to response model
    return LimitsResponseModel.parse_raw(response_json)
