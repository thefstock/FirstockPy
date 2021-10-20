
"""
Datasource for handling markets operations
"""
from pydantic import BaseModel
from ...utils.datasources import NorenRestDataSource
from . import endpoints

from .models import *

class MarketsDataSource(NorenRestDataSource):
  """
  Datasource for handling markets operations
  """
  def get_index_list(self, model: GetIndexListRequestModel, key: str = None) -> GetIndexListResponseModel:
    """
    Get index list

    Args:
      model (GetIndexListRequestModel): The data to be send as GetIndexListRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetIndexListResponseModel: The response as GetIndexListResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_INDEX_LIST, key)
    # convert the request to response model
    return GetIndexListResponseModel.parse_raw(response_json)

  def top_list_names(self, model: TopListNamesRequestModel, key: str = None) -> TopListNamesResponseModel:
    """
    Get top list names

    Args:
      model (TopListNamesRequestModel): The data to be send as TopListNamesRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      TopListNamesResponseModel: The response as TopListNamesResponseModel.
    """
    response_json = self._run_request(model, endpoints.TOP_LIST_NAMES, key)
    # convert the request to response model
    return TopListNamesResponseModel.parse_raw(response_json)

  def top_list(self, model: TopListRequestModel, key: str = None) -> TopListResponseModel:
    """
    Get top list

    Args:
      model (TopListRequestModel): The data to be send as TopListRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      TopListResponseModel: The response as TopListResponseModel.
    """
    response_json = self._run_request(model, endpoints.TOP_LIST, key)
    # convert the request to response model
    return TopListResponseModel.parse_raw(response_json)

  def tp_series(self, model: TimePriceSeriesRequestModel, key: str = None) -> TimePriceSeriesResponseModel:
    """
    Get time price data (Chart data)

    Args:
      model (TimePriceSeriesRequestModel): The data to be send as TimePriceSeriesRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      TimePriceSeriesResponseModel: The response as TimePriceSeriesResponseModel.
    """
    response_json = self._run_request(model, endpoints.TP_SERIES, key)
    # convert the request to response model
    return TimePriceSeriesResponseModel.parse_raw(response_json)

  def get_option_chain(self, model: GetOptionChainRequestModel, key: str = None) -> GetOptionChainResponseModel:
    """
    Get option chain

    Args:
      model (GetOptionChainRequestModel): The data to be send as GetOptionChainRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetOptionChainResponseModel: The response as GetOptionChainResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_OPTION_CHAIN, key)
    # convert the request to response model
    return GetOptionChainResponseModel.parse_raw(response_json)

  def exch_msg(self, model: ExchMessageRequestModel, key: str = None) -> ExchMessageResponseModel:
    """
    Exch message

    Args:
      model (ExchMessageRequestModel): The data to be send as ExchMessageRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      ExchMessageResponseModel: The response as ExchMessageResponseModel.
    """
    response_json = self._run_request(model, endpoints.EXCH_MESSAGE, key)
    # convert the request to response model
    return ExchMessageResponseModel.parse_raw(response_json)

  def get_broker_msg(self, model: GetBrokerMessageRequestModel, key: str = None) -> GetBrokerMessageResponseModel:
    """
    Get broker message

    Args:
      model (GetBrokerMessageRequestModel): The data to be send as GetBrokerMessageRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetBrokerMessageResponseModel: The response as GetBrokerMessageResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_BROKER_MESSAGE, key)
    # convert the request to response model
    return GetBrokerMessageResponseModel.parse_raw(response_json)

  def span_calc(self, model: SpanCalculatorRequestModel, key: str = None) -> SpanCalculatorResponseModel:
    """
    Get broker message

    Args:
      model (SpanCalculatorRequestModel): The data to be send as SpanCalculatorRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      SpanCalculatorResponseModel: The response as SpanCalculatorResponseModel.
    """
    response_json = self._run_request(model, endpoints.SPAN_CALCULATOR, key)
    # convert the request to response model
    return SpanCalculatorResponseModel.parse_raw(response_json)
