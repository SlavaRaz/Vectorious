import requests
from collections import Counter

def test_implant_manufacturer_count(permanent_access_token, base_url):
    
    url = f"{base_url}/v1/implants"
    headers = {
        "Bearer": f"{permanent_access_token}",
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert "implants" in data
    implants = data["implants"]
    assert isinstance(implants, list) 
    
    manufacturer_counts = Counter([implant["manufacturer"] for implant in implants])
    
    assert manufacturer_counts["sct"] == 3 ,f"Expected 3 'sct', got {manufacturer_counts['sct']}"
    assert manufacturer_counts["schott"] == 2 ,f"Expected 2 'schott', got {manufacturer_counts['schott']}"

