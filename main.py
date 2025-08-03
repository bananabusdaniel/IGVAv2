from login import account_login
from instagrapi import Client
from instagrapi.types import User
from utils.profile_scraper import get_source_account_followers, scrape

SOURCE_ACCOUNTS = ["strongful_co"]
profiles = []

# will be depending on which one i want to log into in the future
ACCOUNT = "alt1"

# login to the account
cl = account_login(alt_acc=ACCOUNT)
# list of followers
followers = get_source_account_followers(cl, SOURCE_ACCOUNTS[0], amount=5)

#loop through users
for username in followers:
    try:
        #main scraping function
        profiles.append(scrape(username, cl, SOURCE_ACCOUNTS[0]))
    except Exception as e:
        print(f"Invalid profile: {username}.")
        print(f"Error is {e}")
        print("Moving onto next profile.")
#scrape source accounts (if needed!)