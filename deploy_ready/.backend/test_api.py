import requests
import json

BASE_URL = "https://track.by1.net"

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    print("\nHealth Check:")
    print(response.json())

def test_create_link():
    data = {
        "url": "https://example.com",
        "name": "Example Link"
    }
    response = requests.post(f"{BASE_URL}/api/links", json=data)
    print("\nCreate Link:")
    print(response.json())
    return response.json()['link']['id']

def test_list_links():
    response = requests.get(f"{BASE_URL}/api/links")
    print("\nList Links:")
    print(json.dumps(response.json(), indent=2))

def test_click_link(link_id):
    print(f"\nTesting click for link {link_id}")
    response = requests.get(f"{BASE_URL}/click/{link_id}", allow_redirects=False)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 302:
        print(f"Redirect URL: {response.headers['Location']}")
    else:
        print(response.json())

def test_update_revenue(link_id):
    print(f"\nTesting revenue update for link {link_id}")
    data = {"amount": 10.50}
    response = requests.post(f"{BASE_URL}/api/links/{link_id}/revenue", json=data)
    print(f"Status Code: {response.status_code}")
    print(response.json())

if __name__ == "__main__":
    print("Testing API endpoints...")
    test_health()
    link_id = test_create_link()
    test_click_link(link_id)
    test_update_revenue(link_id)
    test_list_links()  # Should show increased click count and revenue
