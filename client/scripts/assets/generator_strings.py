DATASOURCE = """
\"\"\"
Datasource for handling {module} operations
\"\"\"
from ...utils.datasources import NorenRestDataSource
from . import endpoints
from .models import *

class {classname}DataSource(NorenRestDataSource):
  \"\"\"
  Datasource for handling {module} operations
  \"\"\"
  pass
"""

ENDPOINTS = """
\"\"\"
API endpoint paths stored as constants
\"\"\"

# add your endpoints here
"""

INIT = """
\"\"\"
The {module} module
\"\"\"

from .datasource import *
from .models import *
"""

MODELS_INIT = """
\"\"\"
The request and response models for {module} module
\"\"\"

# import your models here
"""

MODEL = """
\"\"\"
Request and response models for {name} request
\"\"\"
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from ....common.enums import ResponseStatus
from ....utils.decoders import build_loader, datetime_decoder

__all__ = ['{classname}RequestModel', '{classname}ResponseModel']

class {classname}RequestModel(BaseModel):
  \"\"\"
  The request model for {name} endpoint
  \"\"\"
  uid: str
  \"\"\"The user id of the login user\"\"\"

class {classname}ResponseModel(BaseModel):
  \"\"\"
  The response model for {name} endpoint
  \"\"\"
  stat: ResponseStatus
  \"\"\"The {name} success or failure status\"\"\"
  request_time: Optional[datetime]
  \"\"\"It will be present only on successful response.\"\"\"
  emsg: Optional[str]
  \"\"\"Error message if the request failed\"\"\"

  class Config:
    \"\"\"model configuration\"\"\"
    json_loads = build_loader({{
      \"request_time\": datetime_decoder()
    }})
"""

METHOD = """
  def {name}(self, model: {model}RequestModel, key: str = None) -> {model}ResponseModel:
    \"\"\"
    {description}

    Args:
      model ({model}RequestModel): The data to be send as {model}RequestModel.
      key (str, optional): The key obtained on login success. Uses the token in the state if not passed explicitly.

    Returns:
      {model}ResponseModel: The response as {model}ResponseModel.
    \"\"\"
    response_json = self._run_request(model, endpoints.{endpoint}, key)
    # convert the request to response model
    return {model}ResponseModel.parse_raw(response_json)
"""

TEST_SUITE = """
import os
import json
import unittest
from unittest.mock import MagicMock

from py_client import Client, ResponseStatus
from py_client.models import LoginResponseModel
from py_client.modules.{module}.models import *
from py_client.modules.{module} import endpoints

from .common import create_login_model
from .mock import mock_post

class {classname}(unittest.TestCase):
  \"\"\"
  Test {name} module
  \"\"\"

  def setUp(self) -> None:
    self.client = Client(os.getenv('API_URL'), os.getenv('SOCKET_URL'))
    # mock methods
    self.post_mock = MagicMock(wraps=mock_post)
    self.client.{module}.post = self.post_mock
    self.client.users.login = MagicMock(return_value=LoginResponseModel(susertoken='abcdefg'))
    # login
    self.credentials = create_login_model()
    self.token = self.client.login(self.credentials).susertoken
    assert self.token is not None
"""

TEST_CASE = """
  def test_{name}(self):
    model = {model}RequestModel(...)
    response = self.client.{module}.{name}(model)
    with self.subTest('request should be called with proper data'):
      expected_data = {{ ... }}
      expected_body = f'jData={{json.dumps(expected_data)}}&jKey={{self.token}}'
      self.post_mock.assert_called_with(endpoints.{endpoint}, expected_body)
    with self.subTest('response should be parsed properly'):
      assert response is not None
      assert response.stat is not None
      if response.stat == ResponseStatus.OK:
        # check
        pass
      else:
        assert response.emsg is not None
        assert type(response.emsg) == str
"""