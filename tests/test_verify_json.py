import unittest
from src.verify_json import verify_iam_role_policy


class TestVerifyIAMRolePolicy(unittest.TestCase):

    def test_empty_policy(self):
        self.assertTrue(verify_iam_role_policy("test_data/valid_role_policy.json"))
