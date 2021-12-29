Module py_client.modules.funds.datasource
=========================================
Datasource for handling funds operations

Classes
-------

`FundsDataSource(base_url: str = None, interceptors: List[py_client.utils.interceptors.interceptor.Interceptor[py_client.utils.datasources.rest.context.RestContext]] = [], state: Dict[str, Any] = {}, headers: dict = {})`
:   Datasource for handling funds operations
    
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

    `get_content_basket(self, model: py_client.modules.funds.models.get_content_basket.GetContentBasketRequestModel, key: str = None) ‑> py_client.modules.funds.models.get_content_basket.GetContentBasketResponseModel`
    :   Get content basket
        
        Args:
          model (GetContentBasketRequestModel): The data to be send as GetContentBasketRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetContentBasketResponseModel: The response as GetContentBasketResponseModel.

    `get_content_list(self, model: py_client.modules.funds.models.get_content_list.GetContentListRequestModel, key: str = None) ‑> py_client.modules.funds.models.get_content_list.GetContentListResponseModel`
    :   Get content list
        
        Args:
          model (GetContentListRequestModel): The data to be send as GetContentListRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetContentListResponseModel: The response as GetContentListResponseModel.

    `get_max_payout_amount(self, model: py_client.modules.funds.models.get_max_payout_amount.GetMaxPayoutAmountRequestModel, key: str = None) ‑> py_client.modules.funds.models.get_max_payout_amount.GetMaxPayoutAmountResponseModel`
    :   Get max payout amount
        
        Args:
          model (GetMaxPayoutAmountRequestModel): The data to be send as GetMaxPayoutAmountRequestModel.
          key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.
        
        Returns:
          GetMaxPayoutAmountResponseModel: The response as GetMaxPayoutAmountResponseModel.