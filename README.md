# IAM Policy Validator

## Description
This project includes a Python script for validating AWS IAM role policies. It checks  if an input JSON Resource field contains a single asterisk and includes unit tests for various edge cases.

## Prerequisites
- Python 3.11

## Installation
Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/piotrb9/check-aws-iam-role.git check_aws_iam_role
```
```bash
cd check_aws_iam_role
```

## Usage

To run the IAM role policy validation script from the command line, use the following command:
```bash
python src/verify_json.py <path_to_json_file>  
```

## Running Tests
To execute the unit tests, run:
```bash
python -m unittest tests/test_verify_json.py
```
