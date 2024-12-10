import requests

# Define the Auth0 endpoint and credentials
url = "https://dev-lweowtswfm2nqllq.eu.auth0.com/oauth/token"
payload = {
    "client_id": "WtayouTYV74MJtVRESvnNFylLWKtAsF0",
    "client_secret": "9ihwuNsg97nPf2M6w9JbnVYckkpP4a2VAYofvYpZ6GYpeQDA5xIF6N3belbcp1C7",
    "audience": "https://dev-lweowtswfm2nqllq.eu.auth0.com/api/v2/",
    "grant_type": "client_credentials"
}
headers = {
    "Content-Type": "application/json"
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers)

# Parse and print the access token
if response.status_code == 200:
    access_token = response.json().get("access_token")
    print("Access Token:", access_token)
else:
    print("Failed to retrieve token:", response.status_code, response.text)
