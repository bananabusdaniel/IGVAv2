from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

# Load DB URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Define table structure
class Profile(Base):
    __tablename__ = 'profiles'

    #Scraped Info - Simple information extracted using instragapi
    username = Column(String, primary_key=True)
    following = Column(Integer)
    followers = Column(Integer) 
    follower_following_ratio = Column(Integer)
    posts_count = Column(Integer)
    total_likes = Column(Integer)
    total_comments = Column(Integer)
    avg_likes = Column(Integer) # Total likes/num of posts
    avg_comments = Column(Integer) # Total comments/num of posts
    likes_comments_ratio = Column(Integer)
    engagement_rate = Column(Integer) # (avg_likes + avg_comments) / followers
    most_liked_photo_index = Column(Integer) #1 being first photo, x being num of posts
    story_highlights_count = Column(Integer)
    active_story = Column(Boolean)
    days_since_last_post = Column(Integer)
    conversion_status = Column(String) #["scraped", "not_contacted", "messaged", "responded", "converted"]

    #Text base analysis - bio and post text
    bio = Column(Text)
    bio_length_char = Column(Integer)
    bio_sentiment = Column(String) # Emotions-positive/negative
    present_languages = Column(Text) # json - More than several characters - list of strings
    posts_keyword_presence = Column(Text) # json - Repetitive words in posts
    repetitive_hashtags = Column(Text) # json - In bio / posts
    tagging_behaviour = Column(String) # Friends/brands
    link_in_bio = Column(Boolean)
    avg_emoji_per_post = Column(Integer) #Average emoji use per post
    
    #Visual Content Features
    profile_photo = Column(Text) #AI: Short description of profile photo
    face_visible = Column(Boolean) #AI: Important for bot detection!
    is_female = Column(Boolean) #AI: False - male / bot detected
    photos_quality = Column(String) #AI: blurred/high-res
    guessed_age = Column(Integer) #AI:
    has_posted_video = Column(Boolean)

    #AI Conclusions
    is_human = Column(Boolean)
    aesthetic = Column(Text) #Short descriptin of profile aesthetic, hobbies, key features.
    pop_out_feature = Column(Text) #Feature used in message targeting
    conversion_confidence_score = Column(Integer) #Compare profile details above to past conversions/specified details
    profile_score_vector = Column(Text) #json - for later ML
    
    #Debugging
    profile_scrape_time = Column(String) #Date + time object?
    source_account_username = Column(String) #parent account
    error_notes = Column(Text) # json - list of catch errors encountered
