"""
Example usage of save_fcm_token method
"""
from py_client import SaveFCMTokenRequestModel
from argparse import ArgumentParser

from ..base import Example

class SaveFCMTokenExample(Example):

  title: str = 'Save FCM Token'

  def parse_args(self):
    """
    Parse CLI arguments
    """
    parser = ArgumentParser('examples.users.save_fcm_token')
    parser.add_argument('--uid', type=str, help='The user id')
    parser.add_argument('--fcmtkn', type=str, help='The FCM token collected from device')
    parser.add_argument('--token', type=str, help='The token recieved from login')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    model = SaveFCMTokenRequestModel(
      uid=self.args.uid,
      fcmtkn=self.args.fcmtkn
    )
    response = self.client.users.save_fcm_token(model, key=self.args.token)
    return [model, response]

# Run example
example = SaveFCMTokenExample()
example()