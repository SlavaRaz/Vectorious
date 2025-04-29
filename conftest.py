# conftest.py
import pytest
import requests

# Define a CLI option
def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="http://mock-api-env.eba-7vxf99wf.us-east-1.elasticbeanstalk.com",
        help="Base URL for the API tests",
    )

# Create a fixture to access the CLI option easily
@pytest.fixture(scope="session")
def base_url(request):
    # Access the base URL from the command line arguments
    return request.config.getoption("--base-url")

@pytest.fixture(scope="session")
def temp_access_token(base_url):
    
    url = f"{base_url}/v1/login"
    payload = {
        "username": "vectorious@medtech.com",
        "password": "Aa123456"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    data = response.json()
    return data["tempAccessToken"]

@pytest.fixture(scope="session")
def permanent_access_token(base_url, temp_access_token):
    
    url = f"{base_url}/v1/mfa"
    headers = {
        "Bearer": f"{temp_access_token}",
    }
    params = {
        "mfaCode": "879624"
    }
    response = requests.post(url, headers=headers, params=params)
    assert response.status_code == 200
    data = response.json()
    assert "permanentAccessToken" in data
    assert isinstance(data["permanentAccessToken"],str)
    return data["permanentAccessToken"]