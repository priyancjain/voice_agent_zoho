import os
import time
import requests
import json

TOKEN_FILE = "zoho_tokens.json"

CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("ZOHO_REFRESH_TOKEN")
TOKEN_URL = "https://accounts.zoho.in/oauth/v2/token"

def read_tokens():
    """Read access token from environment variables"""
    tokens_json = os.getenv("ZOHO_TOKENS", "{}")  # Read from env
    return json.loads(tokens_json)

def write_tokens(data):
    """Print token update instructions (since we can't write to file)"""
    print("\n🔹 UPDATE your Render environment variable 'ZOHO_TOKENS' with:")
    print(json.dumps(data, indent=4))

def get_access_token():
    tokens = read_tokens()

    if tokens.get("access_token") and time.time() < tokens.get("expires_at", 0):
        return tokens["access_token"]

    response = requests.post(
        TOKEN_URL,
        data={
            "refresh_token": REFRESH_TOKEN,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "refresh_token",
        },
    )

    if response.status_code == 200:
        new_tokens = response.json()
        new_tokens["expires_at"] = time.time() + new_tokens["expires_in"] - 60

        write_tokens(new_tokens)  # Log updated tokens
        return new_tokens["access_token"]

    raise Exception(f"❌ Failed to refresh access token: {response.text}")
