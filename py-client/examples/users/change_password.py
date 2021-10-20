"""
Example usage to reset password
"""
from py_client import ChangePasswordRequestModel
from argparse import ArgumentParser

from ..base import Example

class ChangePasswordExample(Example):

  title: str = 'Change Password'

  def parse_args(self):
    """
    Parse CLI arguments
    """

    parser = ArgumentParser('examples.users.change_password')
    parser.add_argument('--uid', type=str, help='The user id')
    parser.add_argument('--oldpwd', type=str, help='The old password')
    parser.add_argument('--pwd', type=str, help='The new password')
    self.args = parser.parse_args()

  def run(self):
    """
    Run the example
    """
    model = ChangePasswordRequestModel(
      uid=self.args.uid,
      oldpwd=self.args.oldpwd,
      pwd=self.args.pwd
    )
    response = self.client.users.change_password(model)
    return [model, response]

# Run example
example = ChangePasswordExample()
example()