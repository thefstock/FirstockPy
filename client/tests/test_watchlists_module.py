import os
import json
import unittest
from unittest.mock import MagicMock
from datetime import datetime

from py_client import Client, ResponseStatus
from py_client.models import LoginResponseModel
from py_client.modules.watchlists.models import *
from py_client.modules.watchlists import endpoints

from .common import create_login_model
from .mock import mock_post

class TestWatchListsModule(unittest.TestCase):
  """
  Test watchlists module
  """

  def setUp(self) -> None:
    self.client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
    # mock methods
    self.post_mock = MagicMock(wraps=mock_post)
    self.client.watchlists.post = self.post_mock
    self.client.users.login = MagicMock(return_value=LoginResponseModel(susertoken='abcdefg'))
    # login
    self.credentials = create_login_model()
    self.token = self.client.login(self.credentials).susertoken
    assert self.token is not None

  def test_get_names(self):
    model = GetWatchListNamesRequestModel(uid=self.credentials.uid)
    response = self.client.watchlists.get_names(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_NAMES, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.values is not None
        assert type(response.values) == list
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_watchlist(self):
    model = GetWatchListRequestModel(uid=self.credentials.uid, wlname="NSE")
    response = self.client.watchlists.get_watchlist(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid, "wlname": "NSE" }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_WATCHLIST, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.values is not None
        assert type(response.values) == list
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_search_scrips(self):
    model = SearchScripsRequestModel(uid=self.credentials.uid, stext='abcde', exch='NSE')
    response = self.client.watchlists.search_scrips(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid, "stext": "abcde", "exch": "NSE" }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.SEARCH_SCRIPS, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.values is not None
        assert type(response.values) == list
        if len(response.values) > 0:
          item = response.values[0]
          assert item is not None
          assert item.exch is not None
          assert item.tsym is not None
          assert item.token is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_add_scrips(self):
    model = AddScripsRequestModel(uid=self.credentials.uid, wlname='NSE', scrips=['123', '456'])
    response = self.client.watchlists.add_scrips(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid, "wlname": "NSE", "scrips": "123|456"}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.ADD_SCRIPS, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.request_time is not None
        assert type(response.request_time) == datetime
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_delete_scrips(self):
    model = DeleteScripsRequestModel(uid=self.credentials.uid, wlname='NSE', scrips=['123', '456'])
    response = self.client.watchlists.delete_scrips(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid, "wlname": "NSE", "scrips": "123|456"}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.DELETE_SCRIPS, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.request_time is not None
        assert type(response.request_time) == datetime
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_security_info(self):
    model = GetSecurityInfoRequestModel(uid=self.credentials.uid, exch='NSE', token='secrettoken')
    response = self.client.watchlists.get_security_info(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid, "exch": "NSE", "token": "secrettoken"}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_SECURITY_INFO, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.request_time is not None
        assert type(response.request_time) == datetime
        assert response.exch is not None
        assert response.tsym is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_quotes(self):
    model = GetQuotesRequestModel(uid=self.credentials.uid, exch='NSE', token='secrettoken')
    response = self.client.watchlists.get_quotes(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid, "exch": "NSE", "token": "secrettoken"}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_QUOTES, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.request_time is not None
        assert type(response.request_time) == datetime
        assert response.exch is not None
        assert response.tsym is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_predefined_watchlists(self):
    model = GetPredefinedWatchListsRequestModel(uid=self.credentials.uid)
    response = self.client.watchlists.get_predefined_watchlists(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_PREDEFINED_WATCHLISTS, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response.values is not None
      assert type(response.values) == list

  def test_get_predefined_scrips(self):
    model = GetPredefinedScripsRequestModel(uid=self.credentials.uid, wlname='NSE')
    response = self.client.watchlists.get_predefined_scrips(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid, "wlname": "NSE" }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_PREDEFINED_SCRIPS, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.values is not None
        assert type(response.values) == list
        if len(response.values) > 0:
          item = response.values[0]
          assert item is not None
          assert item.exch is not None
          assert item.tsym is not None
          assert item.token is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str
