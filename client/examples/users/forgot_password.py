"""
Example usage of forgot password request
"""
from py_client import ForgotPasswordRequestModel
from argparse import ArgumentParser
from dateutil.parser import parse

from ..base import Example

class ForgotPasswordExample(Example):

  title: str = 'Forgot Password'

  def parse_args(self):
    """
    Parse CLI arguments
    """
    def parse_date(datestring: str):
      return parse(datestring).date()

    parser = ArgumentParser('examples.users.forgot_password')
    parser.add_argument('--uid', type=str, help='The user id')
    parser.add_argument('--pan', type=str, help='The pan of the user')
    parser.add_argument('--dob', type=parse_date, help='The date of birth of the user')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    model = ForgotPasswordRequestModel(
      uid=self.args.uid,
      pan=self.args.pan,
      dob=self.args.dob
    )
    response = self.client.users.forgot_password(model)
    return [model, response]

# Run example
example = ForgotPasswordExample()
example()