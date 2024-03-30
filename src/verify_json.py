import json


def verify_iam_role_policy(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Iterate over the policies in the IAM Role
        for statement in data.get("PolicyDocument").get("Statement"):
            # Check if 'Resource' is a string and equals "*"
            if isinstance(statement.get("Resource"), str) and statement.get("Resource") == "*":
                return False
            # Check if 'Resource' is a list and contains "*"
            elif isinstance(statement.get("Resource"), list) and "*" in statement.get("Resource"):
                return False
        return True

    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return True
    except FileNotFoundError:
        print("File not found.")
        return True
    except TypeError:
        print("Error in the JSON structure.")
        return True
    except AttributeError:
        print("Missing JSON fields.")
        return True
