
from datetime import date
import os
import json
import unittest
from unittest.mock import MagicMock

from py_client import Client, ResponseStatus
from py_client.common.enums import AlertType, AlertValidity, PriceType, RetentionType, TransactionType
from py_client.models import LoginResponseModel
from py_client.modules.alerts.models import *
from py_client.modules.alerts import endpoints

from .common import create_login_model
from .mock import mock_post

class TestAlerts(unittest.TestCase):
  """
  Test alerts module
  """

  def setUp(self) -> None:
    self.client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
    # mock methods
    self.post_mock = MagicMock(wraps=mock_post)
    self.client.alerts.post = self.post_mock
    self.client.users.login = MagicMock(return_value=LoginResponseModel(susertoken='abcdefg'))
    # login
    self.credentials = create_login_model()
    self.token = self.client.login(self.credentials).susertoken
    assert self.token is not None

  def test_set_alert(self):
    model = SetAlertRequestModel(
      uid=self.credentials.uid,
      tsym='AI-222',
      exch='NSE',
      ai_t=AlertType.LTP_A,
      validity=AlertValidity.GTT,
      remarks='random remarks',
      d='1000'
    )
    response = self.client.alerts.set_alert(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "tsym":'AI-222',
        "exch":'NSE',
        "ai_t": 'LTP_A',
        "validity": 'GTT',
        "remarks":'random remarks',
        "d":'1000'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.SET_ALERT, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK or response.stat == 'Oi created':
        response.al_id is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_cancel_alert(self):
    model = CancelAlertRequestModel(
      uid=self.credentials.uid,
      al_id='ABC123'
    )
    response = self.client.alerts.cancel_alert(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "al_id": 'ABC123'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.CANCEL_ALERT, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK or response.stat == 'Oi delete success':
        assert response.al_id is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_modify_alert(self):
    model = ModifyAlertRequestModel(
      uid=self.credentials.uid,
      al_id='12345',
      tsym='AI-222',
      exch='NSE',
      ai_t=AlertType.LTP_A,
      validity=AlertValidity.GTT,
      remarks='random remarks',
      d='1000'
    )
    response = self.client.alerts.modify_alert(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "al_id": '12345',
        "tsym":'AI-222',
        "exch":'NSE',
        "ai_t": 'LTP_A',
        "validity": 'GTT',
        "remarks":'random remarks',
        "d":'1000'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.MODIFY_ALERT, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK or response.stat == 'Oi Replaced':
        assert response.al_id is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_pending_alert(self):
    model = GetPendingAlertRequestModel(uid=self.credentials.uid)
    response = self.client.alerts.get_pending_alert(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_PENDING_ALERT, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.al_id is not None
        assert response.ai_t is not None
        assert response.exch is not None
        assert response.token is not None
        assert response.tsym is not None
        assert response.validity is not None
        assert response.d is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_enabled_alert_types(self):
    model = GetEnabledAlertTypesRequestModel(uid=self.credentials.uid)
    response = self.client.alerts.get_enabled_alert_types(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {"uid": self.credentials.uid}
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_ENABLED_ALERT_TYPES, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.ai_ts is not None
        assert type(response.ai_ts) == list
        if len(response.ai_ts) > 0:
          alt = response.ai_ts[0]
          assert alt is not None
          assert alt.ai_t is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_place_gtt_order(self):
    model = PlaceGttOrderRequestModel(
      uid=self.credentials.uid,
      tsym='AB-212',
      exch='NSE',
      ai_t=AlertType.LTP_A,
      validity=AlertValidity.DAY,
      remarks='random remarks',
      d='12345.00',
      trantype=TransactionType.BUY,
      prctyp=PriceType.DS,
      prd='ABC',
      ret=RetentionType.IOC,
      actid=self.credentials.uid,
      prc=1000,
      qty=25
    )
    response = self.client.alerts.place_gtt_order(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid":self.credentials.uid,
        "tsym":'AB-212',
        "exch":'NSE',
        "ai_t": 'LTP_A',
        "validity": 'DAY',
        "remarks":'random remarks',
        "d":'12345.00',
        "trantype": 'B',
        "prctyp": 'DS',
        "prd":'ABC',
        "ret": 'IOC',
        "actid": self.credentials.uid,
        "prc": '1000',
        "qty": '25'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.PLACE_GTT_ORDER, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK or response.stat == 'Oi created':
        assert response.al_id is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_modify_gtt_order(self):
    model = ModifyGttOrderRequestModel(
      uid=self.credentials.uid,
      tsym='AB-212',
      exch='NSE',
      ai_t=AlertType.LTP_A,
      validity=AlertValidity.DAY,
      remarks='random remarks',
      d='12345.00',
      trantype=TransactionType.BUY,
      prctyp=PriceType.DS,
      prd='ABC',
      ret=RetentionType.IOC,
      actid=self.credentials.uid,
      prc=1000,
      qty=25
    )
    response = self.client.alerts.modify_gtt_order(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid":self.credentials.uid,
        "tsym":'AB-212',
        "exch":'NSE',
        "ai_t": 'LTP_A',
        "validity": 'DAY',
        "remarks":'random remarks',
        "d":'12345.00',
        "trantype": 'B',
        "prctyp": 'DS',
        "prd":'ABC',
        "ret": 'IOC',
        "actid": self.credentials.uid,
        "prc": '1000',
        "qty": '25'
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.MODIFY_GTT_ORDER, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK or response.stat == 'Oi Replaced':
        assert response.al_id is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_cancel_gtt_order(self):
    model = CancelGttOrderRequestModel(
      uid=self.credentials.uid,
      al_id='12345'
    )
    response = self.client.alerts.cancel_gtt_order(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {
        "uid": self.credentials.uid,
        "al_id": "12345"
      }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.CANCEL_GTT_ORDER, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK or response.stat == 'Oi delete success':
        assert response.al_id is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_pending_gtt_order(self):
    model = GetPendingGttOrderRequestModel(uid=self.credentials.uid)
    response = self.client.alerts.get_pending_gtt_order(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_PENDING_GTT_ORDER, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.ai_t is not None
        assert response.al_id is not None
        assert response.tsym is not None
        assert response.token is not None
        assert response.validity is not None
        assert response.actid is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_enabled_gtts(self):
    model = GetEnabledGttsRequestModel(uid=self.credentials.uid)
    response = self.client.alerts.get_enabled_gtts(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_ENABLED_GTTS, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.ai_ts is not None
        assert type(response.ai_ts) == list
        if len(response.ai_ts) > 0:
          ai_t = response.ai_ts[0]
          assert ai_t is not None
          assert ai_t.ai_t is not None
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str

  def test_get_unsettled_trading_date(self):
    model = GetUnsettledTradingDateRequestModel(uid=self.credentials.uid)
    response = self.client.alerts.get_unsettled_trading_date(model)
    with self.subTest('request should be called with proper data'):
      expected_data = { "uid": self.credentials.uid }
      expected_body = f'jData={json.dumps(expected_data)}&jKey={self.token}'
      self.post_mock.assert_called_with(endpoints.GET_UNSETTLED_TRADING_DATE, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        assert response.trd_date is not None
        assert type(response.trd_date) == list
        if len(response.trd_date) > 0:
          trd_d = response.trd_date[0]
          assert trd_d is not None
          assert trd_d.trd_date is not None
          assert type(trd_d.trd_date) == date
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str
