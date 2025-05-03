API Test Automation Suite

This project is a Pytest-based test automation suite for testing the Vectorious API. It verifies login functionality, token authentication, implant data integrity, and other API-related validations.

project-root/
├── conftest.py
├── requirements.txt
├── README.md
├── tests/
│   ├── test_algo_version.py
│   ├── test_failed_first_auth_step.py
│   ├── test_implant_count.py
│   ├── test_passed_first_auth_step.py

1.
git clone https://github.com/SlavaRaz/Vectorious.git
cd Vectorious

2.
python -m venv venv
source venv/bin/activate

3.
Install the dependencies:
pip install -r requirements.txt

To run all tests with the default mock API base URL:
pytest -v

To run with a custom API base URL:
pytest -v --base-url http://mock-api-env.eba-7vxf99wf.us-east-1.elasticbeanstalk.com

Test Coverage:
This suite includes tests for:
Successful and failed login attempts
Temporary and permanent token generation
Decoding implant data
Validating implant algorithm version and sequence
Counting implant manufacturers

📄 Coding Standards:
Code follows PEP 8
Docstrings are written in Google Python Style Guide
Separation of concerns using fixtures and modular test files

📦 Requirements:
Python 3.7+
pytest
requests

  
