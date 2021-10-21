Module py_client.modules.markets.datasource
===========================================
Datasource for handling markets operations

Classes
-------

`MarketsDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   Datasource for handling markets operations
    
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

    `exch_msg(self, model: py_client.modules.markets.models.exch_message.ExchMessageRequestModel, key: str = None) ‑> py_client.modules.markets.models.exch_message.ExchMessageResponseModel`
    :   Exch message
        
        Args:
          model (ExchMessageRequestModel): The data to be send as ExchMessageRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          ExchMessageResponseModel: The response as ExchMessageResponseModel.

    `get_broker_msg(self, model: py_client.modules.markets.models.get_broker_message.GetBrokerMessageRequestModel, key: str = None) ‑> py_client.modules.markets.models.get_broker_message.GetBrokerMessageResponseModel`
    :   Get broker message
        
        Args:
          model (GetBrokerMessageRequestModel): The data to be send as GetBrokerMessageRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetBrokerMessageResponseModel: The response as GetBrokerMessageResponseModel.

    `get_index_list(self, model: py_client.modules.markets.models.get_index_list.GetIndexListRequestModel, key: str = None) ‑> py_client.modules.markets.models.get_index_list.GetIndexListResponseModel`
    :   Get index list
        
        Args:
          model (GetIndexListRequestModel): The data to be send as GetIndexListRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetIndexListResponseModel: The response as GetIndexListResponseModel.

    `get_option_chain(self, model: py_client.modules.markets.models.get_option_chain.GetOptionChainRequestModel, key: str = None) ‑> py_client.modules.markets.models.get_option_chain.GetOptionChainResponseModel`
    :   Get option chain
        
        Args:
          model (GetOptionChainRequestModel): The data to be send as GetOptionChainRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetOptionChainResponseModel: The response as GetOptionChainResponseModel.

    `span_calc(self, model: py_client.modules.markets.models.span_calculator.SpanCalculatorRequestModel, key: str = None) ‑> py_client.modules.markets.models.span_calculator.SpanCalculatorResponseModel`
    :   Get broker message
        
        Args:
          model (SpanCalculatorRequestModel): The data to be send as SpanCalculatorRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          SpanCalculatorResponseModel: The response as SpanCalculatorResponseModel.

    `top_list(self, model: py_client.modules.markets.models.top_list.TopListRequestModel, key: str = None) ‑> py_client.modules.markets.models.top_list.TopListResponseModel`
    :   Get top list
        
        Args:
          model (TopListRequestModel): The data to be send as TopListRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          TopListResponseModel: The response as TopListResponseModel.

    `top_list_names(self, model: py_client.modules.markets.models.top_list_names.TopListNamesRequestModel, key: str = None) ‑> py_client.modules.markets.models.top_list_names.TopListNamesResponseModel`
    :   Get top list names
        
        Args:
          model (TopListNamesRequestModel): The data to be send as TopListNamesRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          TopListNamesResponseModel: The response as TopListNamesResponseModel.

    `tp_series(self, model: py_client.modules.markets.models.time_price_series.TimePriceSeriesRequestModel, key: str = None) ‑> py_client.modules.markets.models.time_price_series.TimePriceSeriesResponseModel`
    :   Get time price data (Chart data)
        
        Args:
          model (TimePriceSeriesRequestModel): The data to be send as TimePriceSeriesRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          TimePriceSeriesResponseModel: The response as TimePriceSeriesResponseModel.