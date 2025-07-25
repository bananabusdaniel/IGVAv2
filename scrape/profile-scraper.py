from instagrapi import Client

#Function: get list of followers of source account
def get_source_account_followers(cl: Client, source_account: str, amount: int) -> list:
    ... #scrape x amount of followers from source

#Function: filter out unfitting profiles
def is_valid_profile(account) -> bool:
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
def concatanate_profile_data(account, source_account) -> dict:
    return {
        "username": account.username,
        "parent_account": source_account,
        "followers": account.follower_count,
        "following": account.following_count,
        "num_posts": account.media_count,
        "total_likes": 0, #posts
        "total_comments": 0, #posts
        "avg_likes": 0, #calc
        "avg_comments": 0, #calc
        "most_liked_photo": 0, #posts
        "story_highlights_count": 0, #easy
        "active_story": False, #easy
        "days_since_last_post": None, #easy
        "bio": account.biography, 
        "bio_length_char": len(account.biography),
        "bio_sentiment": None, #AI
        "present_languages": [], #AI
        "posts_keyword_presence": [], #script/AI?
        "repetitive_hashtags": [], #posts
        "tagging_behaviour": None, #AI?
        "link_in_bio": bool(account.external_url),
        "avg_emoji_per_post": 0, #posts
        "profile_photo": None, #AI
        "face_visible": None, #AI - posts
        "is_female": None, # AI - profile/posts
        "photos_quality": None, #AI - posts
        "guessed_age": None, #AI - posts
        "is_human": None, #AI - posts
        "aesthetic": None, #AI - posts
        "pop_out_feature": None, #AI - posts
        "conversion_confidence_score": None #AI - posts
    }

def store_profile_data() -> None:
    ...
    #store in database. add time delays.



