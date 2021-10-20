"""
The data source for all orders specific requests
"""

from ...utils.datasources import NorenRestDataSource
from . import endpoints

from .models import *

class OrdersDataSource(NorenRestDataSource):
  """
  The datasource for all order specific requests
  """
  
  def place_order(self, model: PlaceOrderRequestModel, key: str = None) -> PlaceOrderResponseModel:
    """
    Place a new order

    Args:
      model (PlaceOrderRequestModel): The data to be send as PlaceOrderRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      PlaceOrderResponseModel: The response as PlaceOrderResponseModel.
    """
    response_json = self._run_request(model, endpoints.PLACE_ORDER, key)
    # convert the request to response model
    return PlaceOrderResponseModel.parse_raw(response_json)

  def modify_order(self, model: ModifyOrderRequestModel, key: str = None) -> ModifyOrderResponseModel:
    """
    Modify an order

    Args:
      model (ModifyOrderRequestModel): The data to be send as ModifyOrderRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      ModifyOrderResponseModel: The response as ModifyOrderResponseModel.
    """
    response_json = self._run_request(model, endpoints.MODIFY_ORDER, key)
    # convert the request to response model
    return ModifyOrderResponseModel.parse_raw(response_json)

  def cancel_order(self, model: CancelOrderRequestModel, key: str = None) -> CancelOrderResponseModel:
    """
    Cancel order

    Args:
      model (CancelOrderRequestModel): The data to be send as CancelOrderRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      CancelOrderResponseModel: The response as CancelOrderResponseModel.
    """
    response_json = self._run_request(model, endpoints.CANCEL_ORDER, key)
    # convert the request to response model
    return CancelOrderResponseModel.parse_raw(response_json)

  def exit_sno_order(self, model: ExitSnoOrderRequestModel, key: str = None) -> ExitSnoOrderResponseModel:
    """
    Exit sno order

    Args:
      model (ExitSnoOrderRequestModel): The data to be send as ExitSnoOrderRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      ExitSnoOrderResponseModel: The response as ExitSnoOrderResponseModel.
    """
    response_json = self._run_request(model, endpoints.EXIT_SNO_ORDER, key)
    # convert the request to response model
    return ExitSnoOrderResponseModel.parse_raw(response_json)

  def get_order_margin(self, model: GetOrderMarginRequestModel, key: str = None) -> GetOrderMarginResponseModel:
    """
    Get order margin

    Args:
      model (GetOrderMarginRequestModel): The data to be send as GetOrderMarginRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetOrderMarginResponseModel: The response as GetOrderMarginResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_ORDER_MARGIN, key)
    # convert the request to response model
    return GetOrderMarginResponseModel.parse_raw(response_json)

  def get_basket_margin(self, model: GetBasketMarginRequestModel, key: str = None) -> GetBasketMarginResponseModel:
    """
    Get basket margin

    Args:
      model (GetBasketMarginRequestModel): The data to be send as GetBasketMarginRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      GetBasketMarginResponseModel: The response as GetBasketMarginResponseModel.
    """
    response_json = self._run_request(model, endpoints.GET_BASKET_MARGIN, key)
    # convert the request to response model
    return GetBasketMarginResponseModel.parse_raw(response_json)

  def order_book(self, model: OrderBookRequestModel, key: str = None) -> OrderBookResponseModel:
    """
    Order book

    Args:
      model (OrderBookRequestModel): The data to be send as OrderBookRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      OrderBookResponseModel: The response as OrderBookResponseModel.
    """
    response_json = self._run_request(model, endpoints.ORDER_BOOK, key)
    # convert the request to response model
    return OrderBookResponseModel.parse_raw(response_json)

  def multileg_order_book(self, model: MultilegOrderBookRequestModel, key: str = None) -> MultilegOrderBookResponseModel:
    """
    Multi Leg Order book

    Args:
      model (MultilegOrderBookRequestModel): The data to be send as MultilegOrderBookRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      MultilegOrderBookResponseModel: The response as MultilegOrderBookResponseModel.
    """
    response_json = self._run_request(model, endpoints.MULTILEG_ORDER_BOOK, key)
    # convert the request to response model
    return MultilegOrderBookResponseModel.parse_raw(response_json)

  def single_order_history(self, model: SingleOrderHistoryRequestModel, key: str = None) -> SingleOrderHistoryResponseModel:
    """
    Single Order History

    Args:
      model (SingleOrderHistoryRequestModel): The data to be send as SingleOrderHistoryRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      SingleOrderHistoryResponseModel: The response as SingleOrderHistoryResponseModel.
    """
    response_json = self._run_request(model, endpoints.SINGLE_ORDER_HISTORY, key)
    # convert the request to response model
    return SingleOrderHistoryResponseModel.parse_raw(response_json)

  def trade_book(self, model: TradeBookRequestModel, key: str = None) -> TradeBookResponseModel:
    """
    Trade Book

    Args:
      model (TradeBookRequestModel): The data to be send as TradeBookRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      TradeBookResponseModel: The response as TradeBookResponseModel.
    """
    response_json = self._run_request(model, endpoints.TRADE_BOOK, key)
    # convert the request to response model
    return TradeBookResponseModel.parse_raw(response_json)

  def position_book(self, model: PositionBookRequestModel, key: str = None) -> PositionBookResponseModel:
    """
    Position Book

    Args:
      model (PositionBookRequestModel): The data to be send as PositionBookRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      PositionBookResponseModel: The response as PositionBookResponseModel.
    """
    response_json = self._run_request(model, endpoints.POSITION_BOOK, key)
    # convert the request to response model
    return PositionBookResponseModel.parse_raw(response_json)

  def convert_product(self, model: ConvertProductRequestModel, key: str = None) -> ConvertProductResponseModel:
    """
    Convert Product

    Args:
      model (ConvertProductRequestModel): The data to be send as ConvertProductRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      ConvertProductResponseModel: The response as ConvertProductResponseModel.
    """
    response_json = self._run_request(model, endpoints.CONVERT_PRODUCT, key)
    # convert the request to response model
    return ConvertProductResponseModel.parse_raw(response_json)
