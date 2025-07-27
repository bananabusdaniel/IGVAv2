
class Profile:
    def __init__(self, username, user_id, source_account, 
                 followers, following, posts_count,
                 days_since_last_post, is_female):
        self.username = username
        self.user_id = user_id
        self.source_account = source_account
        self.followers = followers
        self.following = following
        self.posts_count = posts_count
        self.days_since_last_post = days_since_last_post
        self.is_female = is_female

    # --- USERNAME ---
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if value in ops.get_profile(value):
            raise ValueError(f"Username '{value}' is already in the database")
        self._username = value

    # --- FOLLOWERS ---
    @property
    def followers(self):
        return self._followers

    @followers.setter
    def followers(self, value):
        if value > 15000:
            raise ValueError("Over 15,000 followers")
        self._followers = value

    # --- FOLLOWING ---
    @property
    def following(self):
        return self._following

    @following.setter
    def following(self, value):
        if value < 20:
            raise ValueError("Must follow more than 20 accounts")
        self._following = value

    # --- POSTS COUNT ---
    @property
    def posts_count(self):
        return self._posts_count

    @posts_count.setter
    def posts_count(self, value):
        if value < 5:
            raise ValueError("Must have at least 5 posts")
        self._posts_count = value

    # --- DAYS SINCE LAST POST ---
    @property
    def days_since_last_post(self):
        return self._days_since_last_post

    @days_since_last_post.setter
    def days_since_last_post(self, value):
        if value > 180:
            raise ValueError("Last post was more than 180 days ago")
        self._days_since_last_post = value

    # --- IS FEMALE ---
    @property
    def is_female(self):
        return self._is_female

    @is_female.setter
    def is_female(self, value):
        if not value:
            raise ValueError("User must be female")
        self._is_female = value
    


