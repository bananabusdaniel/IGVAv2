import os
import json
from instagrapi import Client

def account_login(alt_acc: str, base_path: str = "accounts") -> Client:
    
    # Logs into an Instagram alt account using stored credentials and settings (as JSON) if available.
    
    cred_path = os.path.join(base_path, "cred", f"{alt_acc}.json")
    settings_dir = os.path.join(base_path, "settings")
    settings_path = os.path.join(settings_dir, f"{alt_acc}_settings.json")

    # Confirms settings directory if it doesnt exist.
    os.makedirs(settings_dir, exist_ok=True)

    if not os.path.exists(cred_path):
        raise FileNotFoundError(f"Credential file not found: {cred_path}")

    # Read and load alt account credentials JSON
    with open(cred_path, "r") as file:
        creds = json.load(file)

    username = creds["username"]
    password = creds["password"]

    cl = Client()

    #Load alt account settings (cookies, etc)
    if os.path.exists(settings_path):
        print(f"Loading settings for {username}")
        cl.load_settings(settings_path)
    else:
        print(f"No settings found for {username}, logging in fresh...")

    #Login and dump new settings
    cl.login(username, password)
    cl.dump_settings(settings_path)
    print(f"Session saved for {username} at {settings_path}")

    return cl


if __name__ == "__main__":
    client = account_login("alt1")
