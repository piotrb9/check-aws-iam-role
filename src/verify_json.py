import json


def verify_iam_role_policy(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Iterate over the policies in the IAM Role
    for statement in data.get("Statement", []):
        # Check if 'Resource' is a string and equals "*"
        if isinstance(statement.get("Resource"), str) and statement.get("Resource") == "*":
            return False

    return True
