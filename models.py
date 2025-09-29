from sqlalchemy import Column, Integer, String, Float, Computed
from database import Base

class Patient_db(Base):
    __tablename__ = "patient_db"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    address = Column(String)
    age = Column(Integer)
    gender = Column(String)
    height = Column(Float)
    weight = Column(Float)
    
    bmi = Column(Float, Computed("weight / (height * height)"))
    verdict = Column(String, Computed(
        "CASE "
        "WHEN weight / (height * height) < 18.5 THEN 'underweight' "
        "WHEN weight / (height * height) < 25 THEN 'normal' "
        "WHEN weight / (height * height) < 30 THEN 'overweight' "
        "ELSE 'obese' END"
    ))