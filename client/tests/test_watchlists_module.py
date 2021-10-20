import unittest
import os

from py_client import Client, ResponseStatus
from py_client.modules.watchlists.models import *

from .common import create_login_model

class TestWatchListsModule(unittest.TestCase):
  """
  Test watchlists module
  """
  def setUp(self) -> None:
    self.client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
    # login
    self.credentials = create_login_model()
    self.user = self.client.login(self.credentials)
    self.token = self.user.susertoken
    assert self.token is not None
  
  def test_get_names(self):
    model = GetWatchListNamesRequestModel(uid=self.credentials.uid)
    response = self.client.watchlists.get_names(model)
    assert response.stat == ResponseStatus.OK
  def test_get_watchlist(self):
    pass
  def test_search_scrips(self):
    pass
  def test_add_scrips(self):
    pass
  def test_delete_scrips(self):
    pass
  def test_get_security_info(self):
    pass
  def test_get_quotes(self):
    pass
  def test_get_predefined_watchlists(self):
    pass
  def test_get_predefined_scrips(self):
    pass