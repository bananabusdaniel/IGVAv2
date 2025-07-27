#Add profile to database
def add_profile(profile_data: dict):
    session = SessionLocal()
    profile = Profile(**profile_data)
    session.merge(profile)
    session.commit()
    session.close()
