import unittest
from src.verify_json import verify_iam_role_policy


class TestVerifyIAMRolePolicy(unittest.TestCase):

    def test_valid_policy(self):
        self.assertFalse(verify_iam_role_policy("test_data/valid_role_policy.json"))

    def test_empty_file(self):
        self.assertTrue(verify_iam_role_policy("test_data/empty_file.json"))

    def test_no_asterisk(self):
        self.assertTrue(verify_iam_role_policy("test_data/no_asterisk.json"))

    def test_no_resource_field(self):
        self.assertTrue(verify_iam_role_policy("test_data/no_resource_field.json"))

    def test_other_text(self):
        self.assertTrue(verify_iam_role_policy("test_data/other_text.json"))

    def test_no_statement_field(self):
        self.assertTrue(verify_iam_role_policy("test_data/no_statement_field.json"))

