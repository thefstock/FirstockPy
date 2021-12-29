Module py_client.modules.orders.datasource
==========================================
The data source for all orders specific requests

Classes
-------

`OrdersDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   The datasource for all order specific requests
    
    Initialize the RestDataSource
    
    Args:
      base_url (str, optional): The base url for the rest api. Defaults to None.
      interceptors (List[Interceptor[RestContext]], optional): [description]. Defaults to [].
      state (Dict[str, Any]): The current state context. Used to share state across modules.
      headers (dict, optional): The common headers to be used across all requests. Defaults to { 'Content-Type': 'application/x-www-form-urlencoded' }.

    ### Ancestors (in MRO)

    * py_client.utils.datasources.noren.datasource.NorenRestDataSource
    * py_client.utils.datasources.rest.datasource.RestDataSource
    * py_client.utils.stateful.Stateful

    ### Methods

    `cancel_order(self, model: py_client.modules.orders.models.cancel_order.CancelOrderRequestModel, key: str = None) ‑> py_client.modules.orders.models.cancel_order.CancelOrderResponseModel`
    :   Cancel order
        
        Args:
          model (CancelOrderRequestModel): The data to be send as CancelOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          CancelOrderResponseModel: The response as CancelOrderResponseModel.

    `convert_product(self, model: py_client.modules.orders.models.convert_product.ConvertProductRequestModel, key: str = None) ‑> py_client.modules.orders.models.convert_product.ConvertProductResponseModel`
    :   Convert Product
        
        Args:
          model (ConvertProductRequestModel): The data to be send as ConvertProductRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ConvertProductResponseModel: The response as ConvertProductResponseModel.

    `exit_sno_order(self, model: py_client.modules.orders.models.exit_sno_order.ExitSnoOrderRequestModel, key: str = None) ‑> py_client.modules.orders.models.exit_sno_order.ExitSnoOrderResponseModel`
    :   Exit sno order
        
        Args:
          model (ExitSnoOrderRequestModel): The data to be send as ExitSnoOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ExitSnoOrderResponseModel: The response as ExitSnoOrderResponseModel.

    `get_basket_margin(self, model: py_client.modules.orders.models.get_basket_margin.GetBasketMarginRequestModel, key: str = None) ‑> py_client.modules.orders.models.get_basket_margin.GetBasketMarginResponseModel`
    :   Get basket margin
        
        Args:
          model (GetBasketMarginRequestModel): The data to be send as GetBasketMarginRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetBasketMarginResponseModel: The response as GetBasketMarginResponseModel.

    `get_order_margin(self, model: py_client.modules.orders.models.get_order_margin.GetOrderMarginRequestModel, key: str = None) ‑> py_client.modules.orders.models.get_order_margin.GetOrderMarginResponseModel`
    :   Get order margin
        
        Args:
          model (GetOrderMarginRequestModel): The data to be send as GetOrderMarginRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetOrderMarginResponseModel: The response as GetOrderMarginResponseModel.

    `modify_order(self, model: py_client.modules.orders.models.modify_order.ModifyOrderRequestModel, key: str = None) ‑> py_client.modules.orders.models.modify_order.ModifyOrderResponseModel`
    :   Modify an order
        
        Args:
          model (ModifyOrderRequestModel): The data to be send as ModifyOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ModifyOrderResponseModel: The response as ModifyOrderResponseModel.

    `multileg_order_book(self, model: py_client.modules.orders.models.multileg_order_book.MultilegOrderBookRequestModel, key: str = None) ‑> py_client.modules.orders.models.multileg_order_book.MultilegOrderBookResponseModel`
    :   Multi Leg Order book
        
        Args:
          model (MultilegOrderBookRequestModel): The data to be send as MultilegOrderBookRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          MultilegOrderBookResponseModel: The response as MultilegOrderBookResponseModel.

    `order_book(self, model: py_client.modules.orders.models.order_book.OrderBookRequestModel, key: str = None) ‑> py_client.modules.orders.models.order_book.OrderBookResponseModel`
    :   Order book
        
        Args:
          model (OrderBookRequestModel): The data to be send as OrderBookRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          OrderBookResponseModel: The response as OrderBookResponseModel.

    `place_order(self, model: py_client.modules.orders.models.place_order.PlaceOrderRequestModel, key: str = None) ‑> py_client.modules.orders.models.place_order.PlaceOrderResponseModel`
    :   Place a new order
        
        Args:
          model (PlaceOrderRequestModel): The data to be send as PlaceOrderRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          PlaceOrderResponseModel: The response as PlaceOrderResponseModel.

    `position_book(self, model: py_client.modules.orders.models.position_book.PositionBookRequestModel, key: str = None) ‑> py_client.modules.orders.models.position_book.PositionBookResponseModel`
    :   Position Book
        
        Args:
          model (PositionBookRequestModel): The data to be send as PositionBookRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          PositionBookResponseModel: The response as PositionBookResponseModel.

    `single_order_history(self, model: py_client.modules.orders.models.single_order_history.SingleOrderHistoryRequestModel, key: str = None) ‑> py_client.modules.orders.models.single_order_history.SingleOrderHistoryResponseModel`
    :   Single Order History
        
        Args:
          model (SingleOrderHistoryRequestModel): The data to be send as SingleOrderHistoryRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SingleOrderHistoryResponseModel: The response as SingleOrderHistoryResponseModel.

    `trade_book(self, model: py_client.modules.orders.models.trade_book.TradeBookRequestModel, key: str = None) ‑> py_client.modules.orders.models.trade_book.TradeBookResponseModel`
    :   Trade Book
        
        Args:
          model (TradeBookRequestModel): The data to be send as TradeBookRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          TradeBookResponseModel: The response as TradeBookResponseModel.