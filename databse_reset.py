import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from database import Base, engine
import models

def reset_database():
    """Complete database reset - removes old database and creates new one"""
    
    # Close all connections
    engine.dispose()
    
    # Remove the database file if it exists
    db_file = "./patient.db"
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Removed existing database: {db_file}")
    
    # Create fresh database with new schema
    fresh_engine = create_engine("sqlite:///./patient.db", connect_args={"check_same_thread": False})
    
    # Create all tables
    Base.metadata.create_all(bind=fresh_engine)
    print("Created fresh database with new schema")
    
    # Test the autoincrement
    Session = sessionmaker(bind=fresh_engine)
    session = Session()
    
    try:
        # Test insert without providing ID
        test_patient = models.Patient_db(
            name="Test User",
            email="test@example.com",
            address="Test Address",
            age=25,
            gender="male",
            height=1.75,
            weight=70.0
        )
        session.add(test_patient)
        session.commit()
        session.refresh(test_patient)
        print(f"✓ Test successful - Auto-generated ID: {test_patient.id}")
        print(f"✓ BMI calculated: {test_patient.bmi}")
        print(f"✓ Verdict: {test_patient.verdict}")
        
        # Clean up test record
        session.delete(test_patient)
        session.commit()
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        session.rollback()
    finally:
        session.close()

if __name__ == "__main__":
    reset_database()