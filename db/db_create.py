#RUN ONCE AND THEN DELETE!!!!!

from db_models import Base, engine

# Creates tables in the DB
Base.metadata.create_all(bind=engine)
print("Database tables created.")