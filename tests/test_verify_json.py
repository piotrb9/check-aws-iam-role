import unittest
from src.verify_json import verify_iam_role_policy
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class TestVerifyIAMRolePolicy(unittest.TestCase):
    def test_valid_policy(self):
        json_path = os.path.join(BASE_DIR, "test_data/valid_role_policy.json")
        self.assertFalse(verify_iam_role_policy(json_path))

    def test_empty_file(self):
        json_path = os.path.join(BASE_DIR, "test_data/empty_file.json")
        self.assertTrue(verify_iam_role_policy(json_path))

    def test_no_asterisk(self):
        json_path = os.path.join(BASE_DIR, "test_data/no_asterisk.json")
        self.assertTrue(verify_iam_role_policy(json_path))

    def test_no_resource_field(self):
        json_path = os.path.join(BASE_DIR, "test_data/no_resource_field.json")
        self.assertTrue(verify_iam_role_policy(json_path))

    def test_other_text(self):
        json_path = os.path.join(BASE_DIR, "test_data/other_text.json")
        self.assertTrue(verify_iam_role_policy(json_path))

    def test_no_statement_field(self):
        json_path = os.path.join(BASE_DIR, "test_data/no_statement_field.json")
        self.assertTrue(verify_iam_role_policy(json_path))

    def test_valid_policy_extra_fields(self):
        json_path = os.path.join(BASE_DIR, "test_data/valid_role_policy_extra_fields.json")
        self.assertFalse(verify_iam_role_policy(json_path))

    def test_no_file(self):
        json_path = os.path.join(BASE_DIR, "test_data/no_file.json")
        self.assertTrue(verify_iam_role_policy(json_path))

    def test_no_policy_document_field(self):
        json_path = os.path.join(BASE_DIR, "test_data/no_policy_document_field.json")
        self.assertTrue(verify_iam_role_policy(json_path))

    def test_number_resource_field(self):
        json_path = os.path.join(BASE_DIR, "test_data/number_resource_field.json")
        self.assertTrue(verify_iam_role_policy(json_path))

    def test_valid_list_resource_field(self):
        json_path = os.path.join(BASE_DIR, "test_data/valid_list_resource_field.json")
        self.assertFalse(verify_iam_role_policy(json_path))

    def test_empty_list_resource_field(self):
        json_path = os.path.join(BASE_DIR, "test_data/empty_list_resource_field.json")
        self.assertTrue(verify_iam_role_policy(json_path))

    def test_invalid_json_structure(self):
        json_path = os.path.join(BASE_DIR, "test_data/invalid_json_structure.json")
        self.assertTrue(verify_iam_role_policy(json_path))

    def test_valid_single_list_resource_field(self):
        json_path = os.path.join(BASE_DIR, "test_data/valid_single_list_resource_field.json")
        self.assertFalse(verify_iam_role_policy(json_path))


if __name__ == '__main__':
    unittest.main()
