from instagrapi import Client

#Function: get list of followers of source account
def get_source_account_followers(cl: Client, source_account_username: str, amount: int) -> list:
    ... #scrape x amount of followers from source

#Function: filter out unfitting profiles
def is_valid_profile() -> bool:
    ...
    #check basic needs - create file which stores these needs in one place
    #use is_in_database function here too
    '''
    Requirements:
    A. Scraped Features
        1. Public
        2. Under 15k followers, over 20 followers
        3. Over 20 follwing.
        4. Over 5 Posts
        5. Maximum half a year since last post.
        6. Is Woman (+human) + Hebrew used + Age over 16
            a. Bio
            b. Profile photo
            c. Last 6 post photos / captions
    B. Misc Features
        1. Not in database already.


    '''

#Function: filter out already added profiles
def is_in_database() -> bool:
    ...

#Returns dict of single Profile data (after validity check!)
def concatanate_profile_data() -> dict:
    ...
    #just one return with everything - calls a bunch of other functions which return the relevant data


def store_profile_data() -> None:
    ...
    #store in database. add time delays.



