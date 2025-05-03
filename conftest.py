# conftest.py
import pytest
import requests
import json
import base64

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

# Create a fixture to get the temporary access token
@pytest.fixture(scope="session")
def temp_access_token(base_url):
    # Login to get the temporary access toke
    url = f"{base_url}/v1/login"
    payload = {
        "username": "vectorious@medtech.com",
        "password": "Aa123456"
    }
    # Send a POST request to the login endpoint
    response = requests.post(url, json=payload)
    # Check if the response status code is 200
    assert response.status_code == 200
    data = response.json()
    # Return the temporary access token
    return data["tempAccessToken"]

# Create a fixture to get the permanent access token
@pytest.fixture(scope="session")
def permanent_access_token(base_url, temp_access_token):
    # Use the temporary access token to get the permanent access token
    url = f"{base_url}/v1/mfa"
    headers = {
        "Bearer": f"{temp_access_token}",
    }
    params = {
        "mfaCode": "879624"
    }
    # Send a POST request to the MFA endpoint
    response = requests.post(url, headers=headers, params=params)
    assert response.status_code == 200
    data = response.json()
    # Check if the "permanentAccessToken" key is present in the response
    assert "permanentAccessToken" in data
    # Check if the "permanentAccessToken" value is a string
    assert isinstance(data["permanentAccessToken"],str)
    # Return the permanent access token
    return data["permanentAccessToken"]

# Create a fixture to get the implants data
@pytest.fixture(scope="session")
def implants(base_url, permanent_access_token):
    
    url = f"{base_url}/v1/implants"
    headers = {
        "Bearer": f"{permanent_access_token}"
        }
    # Send a GET request to the implants endpoint
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    data = response.json()
    # Check if the response contains the "implants" key
    assert "implants" in data
    implants = data["implants"]
    # Check if the "implants" value is a list
    assert isinstance(implants, list)     
    return data["implants"]

# Create a fixture to decode the implants data
@pytest.fixture(scope="session")
def decoded_implants(implants):
    decoded = []
    for implant in implants:
        coeff_raw = implant["coeffFile"]
        # Decode the base64 encoded string
        coeff_json = json.loads(base64.b64decode(coeff_raw).decode("utf-8"))
        # Insert the decoded JSON into the implant 
        implant["coeffFile"] = coeff_json  
        # Add the implant to the decoded list
        decoded.append(implant)
    return decoded
