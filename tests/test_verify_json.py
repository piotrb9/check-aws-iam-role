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

    def test_valid_policy_extra_fields(self):
        self.assertFalse(verify_iam_role_policy("test_data/valid_role_policy_extra_fields.json"))

    def test_no_file(self):
        self.assertTrue(verify_iam_role_policy("test_data/no_file.json"))

    def test_no_policy_document_field(self):
        self.assertTrue(verify_iam_role_policy("test_data/no_policy_document_field.json"))

    def test_number_resource_field(self):
        self.assertTrue(verify_iam_role_policy("test_data/number_resource_field.json"))

    def test_valid_list_resource_field(self):
        self.assertFalse(verify_iam_role_policy("test_data/valid_list_resource_field.json"))

    def test_empty_list_resource_field(self):
        self.assertTrue(verify_iam_role_policy("test_data/empty_list_resource_field.json"))

    def test_invalid_json_structure(self):
        self.assertTrue(verify_iam_role_policy("test_data/invalid_json_structure.json"))

    def test_valid_single_list_resource_field(self):
        self.assertFalse(verify_iam_role_policy("test_data/valid_single_list_resource_field.json"))


if __name__ == '__main__':
    unittest.main()
