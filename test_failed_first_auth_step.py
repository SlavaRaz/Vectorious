import requests

def test_failed_incorrect_credentials(base_url):
    
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
