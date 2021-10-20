"""
Example usage to retrieve HS token
"""
import json
from argparse import ArgumentParser

from ..base import Example

class ValidateHsTokenExample(Example):

  def parse_args(self):
    """
    Parse CLI arguments
    """
    parser = ArgumentParser('examples.users.validate_hs_token')
    parser.add_argument('--login_id', type=str, help='The sLoginId received from Initiator site')
    parser.add_argument('--token', type=str, help='The hs token to validate')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    response = self.client.users.validate_hs_token(self.args.login_id, self.args.token)
    request = json.dumps({ "login_id": self.args.login_id, "token": self.args.token }, indent=2)
    self.print_output(request, str(response), title='example.validate_hs_token')

# Run example
example = ValidateHsTokenExample()
example.run()