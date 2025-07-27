from db.models import SessionLocal, Profile
from sqlalchemy.orm.exc import NoResultFound

#Add profile to database
def add_profile(profile_data: dict):
    session = SessionLocal()
    profile = Profile(**profile_data)
    session.merge(profile)
    session.commit()
    session.close()

#Change field of profile in database
def alter_profile(username: str, field: str, new_value: str) -> None:
    session = SessionLocal()
    try:
        profile = session.query(Profile).filter_by(username=username).one()
        setattr(profile, field, new_value)
        session.commit()
    except NoResultFound:
        print(f"Profile {username} not found.")
    finally:
        session.close()

#Get all the profiles from database
def get_all_profiles() -> list:
    session = SessionLocal()
    profiles = session.query(Profile).all()
    session.close()
    return profiles #list of Profile objects

#Get specific Profile from database
def get_profile(username: str) -> Profile:
    session = SessionLocal()
    try:
        profile = session.query(Profile).filter_by(username=username).one()
        return profile
    except NoResultFound:
        print(f"{username} was not found")
        return None
    finally:
        session.close()