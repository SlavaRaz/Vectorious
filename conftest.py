# conftest.py

import pytest

# Define a CLI option
def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="http://mock-api-env.eba-7vxf99wf.us-east-1.elasticbeanstalk.com",
        help="Base URL for the API tests",
    )

# Create a fixture to access the CLI option easily
@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url")
