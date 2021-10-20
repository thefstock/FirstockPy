import os
from py_client import LoginRequestModel, RequestSourceType
# load env files
from dotenv import load_dotenv
load_dotenv()

__all__ = ['create_login_model']

def create_login_model():
  model = LoginRequestModel(
    apkversion = os.getenv('APK_VERSION'),
    appkey = os.getenv('APP_KEY'),
    vc = os.getenv('VC'),
    uid = os.getenv('UID'),
    pwd = os.getenv('PASSWORD'),
    factor2 = os.getenv("FACTOR2"),
    imei = "134243434",
    source = RequestSourceType.API
  )
  return model