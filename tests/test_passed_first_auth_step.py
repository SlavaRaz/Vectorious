import requests

def test_passed_correct_credentials(base_url):
    """
    Test that the login API accepts valid credentials.

    Sends a login request using a correct username and password,
    and verifies:
      - The response status code is 200.
      - The response includes a 'tempAccessToken' of type string.

    Args:
        base_url (str): The base URL of the API.

    Raises:
        AssertionError: If the login fails or the token is missing or incorrect type.
    """
    login_url = f"{base_url}/v1/login"
    payload = {
    "username": "vectorious@medtech.com",
    "password": "Aa123456"
    }
    # Sending a POST request with correct credentials
    response = requests.post(login_url, json=payload)
    # Checking the response status code
    assert response.status_code == 200
    data = response.json()
    # Checking if the "tempAccessToken" key is present in the response
    assert "tempAccessToken" in data 
    # Checking if the "tempAccessToken" value is a string 
    assert isinstance(data["tempAccessToken"], str)  
