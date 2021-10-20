"""
The client combines all the modules and abstracts the inner logic
"""

from .modules.users import LoginRequestModel, LogoutRequestModel
from .modules.users import UserDataSource
from .modules.watchlists import WatchListDataSource
from .modules.orders import OrdersDataSource
from .modules.markets import MarketsDataSource
from .modules.alerts import AlertsDataSource
from .modules.funds import FundsDataSource
from .modules.holdings_limits import HoldingsLimitsDataSource
from .modules.holdings_limits import HoldingsRequestModel, LimitsRequestModel
from .utils.stateful import Stateful

__all__ = ['Client']

class Client(Stateful):
  """
  The python client for communicating with external api
  """
  def __init__(self, base_url: str = None) -> None:
    """
    Initialize the client

    Args:
      base_url (str, optional): The base url for the rest api endpoint. Defaults to None.
    """
    super().__init__({
      "token": None
    })
    self.__setup__()
    self.__users = UserDataSource(base_url, interceptors=self._interceptors, state = self.state)
    self.__watchlists = WatchListDataSource(base_url, interceptors=self._interceptors, state=self.state)
    self.__orders = OrdersDataSource(base_url, interceptors=self._interceptors, state=self.state)
    self.__markets = MarketsDataSource(base_url, interceptors=self._interceptors, state=self.state)
    self.__alerts = AlertsDataSource(base_url, interceptors=self._interceptors, state=self.state)
    self.__funds = FundsDataSource(base_url, interceptors=self._interceptors, state=self.state)
    self.__hl = HoldingsLimitsDataSource(base_url, interceptors=self._interceptors, state=self.state)

  def __setup__(self) -> None:
    """
    Initial setup for the client
    """
    self._interceptors = []

  @property
  def state(self):
    """The current client state"""
    return self.__state__

  @property
  def users(self) -> UserDataSource:
    """
    The user module datasource
    """
    return self.__users

  @property
  def watchlists(self) -> WatchListDataSource:
    """
    The watchlists module datasource
    """
    return self.__watchlists

  @property
  def orders(self) -> OrdersDataSource:
    """
    The orders module datasource
    """
    return self.__orders

  @property
  def markets(self) -> MarketsDataSource:
    """
    The markets module datasource
    """
    return self.__markets

  @property
  def alerts(self) -> AlertsDataSource:
    """
    The alerts module datasource
    """
    return self.__alerts

  @property
  def funds(self) -> FundsDataSource:
    """
    The funds module datasource
    """
    return self.__funds

  def login(self, model: LoginRequestModel):
    """
    Login user. Alias for ```client.users.login```

    Args:
      model (LoginRequestModel): The data to be send as LoginRequestModel instance.

    Returns:
      LoginResponseModel: The response from login request as LoginResponseModel instance.
    """
    response = self.__users.login(model)
    # set state token if successful
    if response.susertoken is not None:
      self.set_state('token', response.susertoken)
    return response

  def logout(self, model: LogoutRequestModel, key: str = None):
    """
    Logout user. Alias for ```client.users.logout```

    Args:
      model (LogoutRequestModel): The data to be send as LogoutRequestModel instance
      key (str): The key obtained on login success

    Returns:
      LogoutResponseModel: The response from logout request as LogoutResponseModel instance
    """
    return self.__users.logout(model, key)

  def holdings(self, model: HoldingsRequestModel, key: str):
    """
    Get holdings

    Args:
      model (HoldingsRequestModel): The data to be send as HoldingsRequestModel.
      key (str): The key obtained on login success
    
    Returns:
      HoldingsResponseModel: The response as HoldingsResponseModel.
    """
    return self.__hl.holdings(model, key)

  def limits(self, model: LimitsRequestModel, key: str = None):
    """
    Limits

    Args:
      model (LimitsRequestModel): The data to be send as LimitsRequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      LimitsResponseModel: The response as LimitsResponseModel.
    """
    return self.__hl.limits(model, key)