import unittest
from src.verify_json import verify_iam_role_policy


class TestVerifyIAMRolePolicy(unittest.TestCase):

    def test_valid_policy(self):
        self.assertFalse(verify_iam_role_policy("test_data/valid_role_policy.json"))

    def test_empty_file(self):
        self.assertTrue(verify_iam_role_policy("test_data/empty_file.json"))