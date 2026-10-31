import os

import httpx

# Set API_EMAIL and API_PASSWORD to the local course user's credentials.
login_payload = {
    "email": os.environ["API_EMAIL"],
    "password": os.environ["API_PASSWORD"],
}

login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", json=login_payload
)
login_response_data = login_response.json()

access_token = login_response_data["token"]["accessToken"]
user_me_headers = {"Authorization": f"Bearer {access_token}"}
user_me_response = httpx.get(
    "http://localhost:8000/api/v1/users/me", headers=user_me_headers
)

print(user_me_response.json())
print(user_me_response.status_code)
