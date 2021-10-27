
import os
import json
import unittest
import pytest
from datetime import datetime
from unittest.mock import MagicMock

from py_client import Client, ResponseStatus
from py_client.models import LoginResponseModel
from py_client.modules.markets.models import *
from py_client.modules.markets import endpoints

from .common import create_login_model
from .mock import mock_post

class TestMarkets(unittest.TestCase):
  """
  Test markets module
  """

  def setUp(self) -> None:
    self.client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
    # mock methods
    self.post_mock = MagicMock(wraps=mock_post)
    self.client.markets.post = self.post_mock
    self.client.users.login = MagicMock(return_value=LoginResponseModel(susertoken='abcdefg'))
    # login
    self.credentials = create_login_model()
    self.token = self.client.login(self.credentials).susertoken
    assert self.token is not None

  def test_get_index_list(self):
    model = GetIndexListRequestModel(
      uid=self.credentials.uid,
      exch='NSE'
    )
    response = self.client.markets.get_index_list(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid, "exch": "NSE"}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_INDEX_LIST, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.values is not None
        assert type(response.values) == list
        if len(response.values) > 0:
          value = response.values[0]
          assert value is not None
          assert value.idxname is not None
          assert value.token is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_top_list_names(self):
    model = TopListNamesRequestModel(
      uid=self.credentials.uid,
      exch='NSE'
    )
    response = self.client.markets.top_list_names(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid, "exch": "NSE"}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.TOP_LIST_NAMES, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.values is not None
        assert type(response.values) == list
        if len(response.values) > 0:
          value = response.values[0]
          assert value is not None
          assert value.bskt is not None
          assert value.crt is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_top_list(self):
    model = TopListRequestModel(
      uid=self.credentials.uid,
      exch='NSE',
      tb='T',
      bskt='ABCDE',
      crt='LTP'
    )
    response = self.client.markets.top_list(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "exch": 'NSE',
        "tb": 'T',
        "bskt": 'ABCDE',
        "crt": 'LTP'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.TOP_LIST, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.values is not None
        assert type(response.values) == list
        if len(response.values) > 0:
          value = response.values[0]
          assert value.tsym is not None
          assert value.lp is not None
          assert value.value is not None
          assert value.pc is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_tp_series(self):
    model = TimePriceSeriesRequestModel(
      uid=self.credentials.uid,
      exch='NSE',
      token='abcdef',
      st=datetime(2012,2,28,10,30,30),
      et=datetime(2012,2,28,10,30,30)
    )
    response = self.client.markets.tp_series(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "exch": 'NSE',
        "token": 'abcdef',
        "st": "1330405230",
        "et": "1330405230"
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.TP_SERIES, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.time is not None
        assert type(response.time) == datetime
        assert response.v is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_broker_msg(self):
    model = GetBrokerMessageRequestModel(uid=self.credentials.uid)
    response = self.client.markets.get_broker_msg(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_BROKER_MESSAGE, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.dmsg is not None
        assert response.norentm is not None
        assert type(response.norentm) == datetime
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  @pytest.mark.skip(reason='No response sample available')
  def test_get_option_chain(self):
    model = GetOptionChainRequestModel(...)
    response = self.client.markets.get_option_chain(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { ... }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_OPTION_CHAIN, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        # check
        pass
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  @pytest.mark.skip(reason='No response sample available')
  def test_exch_msg(self):
    model = ExchMessageRequestModel(...)
    response = self.client.markets.exch_msg(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { ... }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.EXCH_MESSAGE, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        # check
        pass
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  @pytest.mark.skip(reason='No response sample available')
  def test_span_calc(self):
    model = SpanCalculatorRequestModel(...)
    response = self.client.markets.span_calc(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { ... }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.SPAN_CALCULATOR, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        # check
        pass
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str
