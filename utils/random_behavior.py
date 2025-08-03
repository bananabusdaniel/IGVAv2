"""Utility functions for simulating random human-like Instagram activity."""

import random
import time
from typing import List, Optional

from instagrapi import Client


def random_delay(min_sec: float, max_sec: float) -> None:
    """Sleep for a random duration between ``min_sec`` and ``max_sec`` seconds."""
    time.sleep(random.uniform(min_sec, max_sec))


def take_short_break(min_minutes: float = 10, max_minutes: float = 30) -> None:
    """Sleep for a random duration between ``min_minutes`` and ``max_minutes`` minutes."""
    random_delay(min_minutes * 60, max_minutes * 60)


def scroll_home_feed_randomly(
    cl: Client,
    min_posts: int = 3,
    max_posts: int = 10,
    min_delay: float = 1,
    max_delay: float = 2,
    min_likes: int = 1,
    max_likes: int = 2,
) -> None:
    """View posts from the home feed and optionally like some of them.

    Parameters default to simulating viewing 3–10 posts, sleeping 1–2 seconds
    between posts, and liking 1–2 of them.
    """
    amount = random.randint(min_posts, max_posts)
    medias = cl.feed_timeline(amount=amount)

    for _ in medias:
        random_delay(min_delay, max_delay)

    like_count = random.randint(min_likes, max_likes)
    for media in random.sample(medias, k=min(like_count, len(medias))):
        cl.media_like(media.pk)


def randomly_watch_stories(
    cl: Client,
    min_users: int = 1,
    max_users: int = 5,
    min_delay: float = 3,
    max_delay: float = 10,
) -> None:
    """Watch stories of randomly selected followed users."""
    following = list(cl.user_following(cl.user_id, amount=50).values())
    if not following:
        return

    count = random.randint(min_users, max_users)
    users = random.sample(following, k=min(count, len(following)))
    for user in users:
        stories = cl.user_stories(user.pk)
        for story in stories:
            cl.story_view(story.pk)
        random_delay(min_delay, max_delay)


def browse_explore_hashtags(
    cl: Client,
    hashtags: Optional[List[str]] = None,
    min_posts: int = 5,
    max_posts: int = 8,
    min_delay: float = 1,
    max_delay: float = 2,
    min_likes: int = 1,
    max_likes: int = 2,
) -> None:
    """Browse posts from a random hashtag and optionally like some."""
    if hashtags is None:
        hashtags = ["travel", "food", "nature", "art", "photography"]
    tag = random.choice(hashtags)

    medias = cl.hashtag_medias_recent(tag, amount=random.randint(min_posts, max_posts))
    for _ in medias:
        random_delay(min_delay, max_delay)

    like_count = random.randint(min_likes, max_likes)
    for media in random.sample(medias, k=min(like_count, len(medias))):
        cl.media_like(media.pk)


def random_profile_crawl(
    cl: Client,
    username: str,
    min_posts: int = 3,
    max_posts: int = 5,
    min_delay: float = 2,
    max_delay: float = 5,
    min_likes: int = 0,
    max_likes: int = 3,
) -> None:
    """Visit a profile, scroll through posts, and optionally like some."""
    user_id = cl.user_id_from_username(username)
    medias = cl.user_medias(user_id, amount=random.randint(min_posts, max_posts))

    for _ in medias:
        random_delay(min_delay, max_delay)

    like_count = random.randint(min_likes, max_likes)
    for media in random.sample(medias, k=min(like_count, len(medias))):
        cl.media_like(media.pk)
