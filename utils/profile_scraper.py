from login import account_login
from instagrapi import Client
from db import ops
from igv_types.profile_candidate import Profile
from datetime import datetime, timezone

#Function: get list of followers of source account
def get_source_account_followers(cl: Client, source_account: str, amount: int) -> list:
    followers = []
    user_id = cl.user_id_from_username(source_account)
    followers_dict = cl.user_followers(user_id, amount)
    for uid, user in followers_dict.items():
        followers.append(user.username)
    return followers

#Main scraping function
def scrape(username: str, cl: Client, source_account: str = "") -> Profile:
    # Skip immediately if the profile already exists in the database.  This
    # check is inexpensive and prevents wasting tokens on profiles we have already processed.
    if ops.get_profile(username):
        raise ValueError(f"Username '{username}' is already in the database")

    # Fetch basic user info.  This single call returns several lightweight
    # metrics which we validate progressively before performing any additional API requests.
    user = cl.user_info_by_username(username)
    user_id = user.pk

    followers = user.follower_count
    if followers < 10 or followers > 15000:
        raise ValueError("Followers must be between 10 and 15,000")

    following = user.following_count
    if following < 20:
        raise ValueError("Must follow more than 20 accounts")

    posts_count = user.media_count
    if posts_count < 5:
        raise ValueError("Must have at least 5 posts")

    # Only if the cheaper checks pass do we query for the user's latest post,
    # as this requires an additional request and therefore more tokens.
    medias = cl.user_medias(user_id, amount=1)
    if not medias:
        raise ValueError("Unable to determine last post date")
    last_post = medias[0]
    now = datetime.now(timezone.utc)
    days_since_last_post = (now - last_post.taken_at).days
    if days_since_last_post > 180:
        raise ValueError("Last post was more than 180 days ago")

    # Placeholder for future gender detection logic. For now, assume True so
    # that validation relies solely on the `Profile` setters.
    is_female = True

    return Profile(
        username=username,
        user_id=user_id,
        source_account=source_account,
        followers=followers,
        following=following,
        posts_count=posts_count,
        days_since_last_post=days_since_last_post,
        is_female=is_female,
    )
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







'''#Returns dict of single Profile data (after validity check!)
def concatanate_profile_data(account, source_account) -> dict:
    return {
        "username": account.username,
        "user_id": ...,
        "source_account": source_account,
        "followers": account.follower_count,
        "following": account.following_count,
        "posts_count": account.media_count,
        "total_likes": 0, #posts
        "total_comments": 0, #posts
        "avg_likes": 0, #calc
        "avg_comments": 0, #calc
        "most_liked_photo_index": 0, #posts
        "story_highlights_count": 0, #easy
        "active_story": False, #easy
        "days_since_last_post": None, #easy
        "follower_following_ratio": None,
        "likes_comments_ratio": None,
        "engagement_rate": None,
        "profile_scrape_time": None, #datetime module
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
        "conversion_confidence_score": None, #AI - posts
        "error_notes": None,
        "profile_score_vector": None
    }

def store_profile_data() -> None:
    pass
    #store in database. add time delays.
'''


