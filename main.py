from login import account_login
from instagrapi import Client
from instagrapi.types import User
from utils.profile_scraper import get_source_account_followers, scrape

SOURCE_ACCOUNTS = ["pilatesgirl"]

# will be depending on which one i want to log into in the future
ACCOUNT = "alt1"

# login to the account
cl = account_login(ACCOUNT)
# list of followers
followers = get_source_account_followers(cl, SOURCE_ACCOUNTS[0], amount=500)

#loop through users
for username in followers:
    try:
        #main scraping function
        scrape(username, cl)
    except:
        print(f"Invalid profile with username {username}")
#scrape source accounts (if needed!)