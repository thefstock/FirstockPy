"""
Example usage of client to set device pin
"""
from py_client import SetDevicePinRequestModel, RequestSourceType
from argparse import ArgumentParser

from ..base import Example

class SetDevicePinExample(Example):

  title: str = 'Set Device Pin'

  def parse_args(self):
    """
    Parse CLI arguments
    """

    parser = ArgumentParser('examples.users.set_device_pin')
    parser.add_argument('--uid', type=str, help='The user id')
    parser.add_argument('--imei', type=str, help='The IMEI or device unique fingerprint')
    parser.add_argument('--dpin', type=str, help='The new pin')
    parser.add_argument('--token', type=str, help='The token recieved from login')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    model = SetDevicePinRequestModel(
      uid=self.args.uid,
      imei=self.args.imei,
      dpin=self.args.dpin,
      source=RequestSourceType.API
    )
    response = self.client.users.set_device_pin(model, key=self.args.token)
    return [model, response]

# Run example
example = SetDevicePinExample()
example()