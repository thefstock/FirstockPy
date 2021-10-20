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