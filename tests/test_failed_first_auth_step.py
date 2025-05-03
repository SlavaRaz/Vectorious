import requests

def test_failed_incorrect_credentials(base_url):
    """
    Test that the login API returns the correct response for invalid credentials.

    Sends a POST request with incorrect username and password, 
    and verifies that:
      - The response status code is 404 (Not Found).
      - The response does not contain a 'tempAccessToken' key.

    Args:
        base_url (str): The base URL of the API.

    Raises:
        AssertionError: If the response status is not 404, or if 'tempAccessToken' is found.
    """
    login_url = f"{base_url}/v1/login"
    payload = {
    "username": "wrong@medtech.com",
    "password": "wrongAa123456"
    }
    # Sending a POST request with incorrect credentials
    response = requests.post(login_url, json=payload)
    # Checking the response status code
    assert response.status_code == 404
    
    try:
        # Attempting to parse the response as JSON
        data = response.json()
        # Checking if the "tempAccessToken" key is not present in the response
        assert "tempAccessToken" not in data
    except ValueError:
        print("No JSON received in response")
