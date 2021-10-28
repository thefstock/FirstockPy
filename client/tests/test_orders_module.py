
from datetime import datetime
import os
import json
import unittest
import pytest
from unittest.mock import MagicMock

from py_client import Client, ResponseStatus
from py_client.common.enums import PriceType, RetentionType, TransactionType
from py_client.models import LoginResponseModel
from py_client.modules.orders.models import *
from py_client.modules.orders import endpoints

from .common import create_login_model
from .mock import mock_post

class TestOrders(unittest.TestCase):
  """
  Test orders module
  """

  def setUp(self) -> None:
    self.client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
    # mock methods
    self.post_mock = MagicMock(wraps=mock_post)
    self.client.orders.post = self.post_mock
    self.client.users.login = MagicMock(return_value=LoginResponseModel(susertoken='abcdefg'))
    # login
    self.credentials = create_login_model()
    self.token = self.client.login(self.credentials).susertoken
    assert self.token is not None

  def test_place_order(self):
    model = PlaceOrderRequestModel(
      uid=self.credentials.uid,
      actid=self.credentials.uid,
      exch='NSE',
      tsym='ABCD',
      qty=20,
      prc=100,
      prd='ABC123',
      trantype=TransactionType.SELL,
      prctyp=PriceType.DS,
      ret=RetentionType.DAY
    )
    response = self.client.orders.place_order(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "actid": self.credentials.uid,
        "exch": 'NSE',
        "tsym": 'ABCD',
        "qty": "20",
        "prc": "100",
        "prd": "ABC123",
        "trantype": "S",
        "prctyp": "DS",
        "ret": "DAY"
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.PLACE_ORDER, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.norenordno is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_modify_order(self):
    model = ModifyOrderRequestModel(
      uid=self.credentials.uid,
      norenordno='20052000000017',
      exch='NSE',
      tsym='ABCD'
    )
    response = self.client.orders.modify_order(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "exch": 'NSE',
        "norenordno":'20052000000017',
        "tsym": 'ABCD'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.MODIFY_ORDER, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.result is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_cancel_order(self):
    model = CancelOrderRequestModel(
      uid=self.credentials.uid,
      norenordno='20052000000017',
    )
    response = self.client.orders.cancel_order(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "norenordno":'20052000000017',
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.CANCEL_ORDER, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.result is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  @pytest.mark.skip(reason='No response sample available')
  def test_exit_sno_order(self):
    model = ExitSnoOrderRequestModel(
      uid=self.credentials.uid,
      norenordno='20052000000017',
      prd='ABC123'
    )
    response = self.client.orders.exit_sno_order(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "norenordno":'20052000000017',
        "prd": 'ABC123'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.EXIT_SNO_ORDER, expected_body)
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
  def test_get_order_margin(self):
    model = GetOrderMarginRequestModel(...)
    response = self.client.orders.get_order_margin(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { ... }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_ORDER_MARGIN, expected_body)
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
  def test_get_basket_margin(self):
    model = GetBasketMarginRequestModel(...)
    response = self.client.orders.get_basket_margin(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { ... }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_BASKET_MARGIN, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        # check
        pass
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_order_book(self):
    model = OrderBookRequestModel(
      uid=self.credentials.uid,
      prd='ABC123'
    )
    response = self.client.orders.order_book(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "prd": 'ABC123'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.ORDER_BOOK, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.exch is not None
        assert response.prc is not None
        assert response.qty is not None
        assert response.prd is not None
        assert response.tsym is not None
        assert response.norenordno is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  @pytest.mark.skip(reason='No response sample available')
  def test_multileg_order_book(self):
    model = MultilegOrderBookRequestModel(...)
    response = self.client.orders.multileg_order_book(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { ... }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.MULTILEG_ORDER_BOOK, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.exch is not None
        assert response.prc is not None
        assert response.qty is not None
        assert response.prd is not None
        assert response.tsym is not None
        assert response.norenordno is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_single_order_history(self):
    model = SingleOrderHistoryRequestModel(
      uid=self.credentials.uid,
      norenordno='20052000000017',
    )
    response = self.client.orders.single_order_history(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "norenordno":'20052000000017',
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.SINGLE_ORDER_HISTORY, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.exch is not None
        assert response.prc is not None
        assert response.qty is not None
        assert response.prd is not None
        assert response.tsym is not None
        assert response.norenordno is not None
        assert response.uid is not None
        assert response.actid is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_position_book(self):
    model = PositionBookRequestModel(
      uid=self.credentials.uid,
      actid=self.credentials.uid
    )
    response = self.client.orders.position_book(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "actid": self.credentials.uid
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.POSITION_BOOK, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.exch is not None
        assert response.prd is not None
        assert response.tsym is not None
        assert response.uid is not None
        assert response.actid is not None
        assert response.pp is not None
        assert response.ls is not None
        assert response.ti is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_convert_product(self):
    model = ConvertProductRequestModel(
      uid=self.credentials.uid,
      tsym='ABCD',
      qty=1000.0,
      actid=self.credentials.uid,
      prd='ABC123',
      prevprd='BCD234',
      trantype=TransactionType.BUY,
      postype='CF'
    )
    response = self.client.orders.convert_product(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid":self.credentials.uid,
        "tsym":'ABCD',
        "qty":1000.0,
        "actid":self.credentials.uid,
        "prd":'ABC123',
        "prevprd":'BCD234',
        "trantype":'B',
        "postype":'CF'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.CONVERT_PRODUCT, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.request_time is not None
        assert type(response.request_time) == datetime
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_trade_book(self):
    model = TradeBookRequestModel(
      uid=self.credentials.uid,
      actid=self.credentials.uid
    )
    response = self.client.orders.trade_book(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "actid": self.credentials.uid
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.TRADE_BOOK, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.exch is not None
        assert response.prd is not None
        assert response.tsym is not None
        assert response.uid is not None
        assert response.actid is not None
        assert response.pp is not None
        assert response.ls is not None
        assert response.ti is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str
