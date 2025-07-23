from db_models import SessionLocal, Profile
from sqlalchemy.orm.exc import NoResultFound

#Add profile to database
def add_profile(profile_data: dict):
    session = SessionLocal()
    profile = Profile(**profile_data)
    session.merge(profile)
    session.commit()
    session.close()

#Get all the profiles from database
def get_all_profiles() -> list:
    session = SessionLocal()
    profiles = session.query(Profile).all()
    session.close()
    return profiles #list of Profile objects
