from sqlalchemy import Column, Integer, String, Float, Computed
from database import base

class Patient_db(base):
    __tablename__ = "patient_db"  

    name = Column(String, primary_key=True)
    city = Column(String)
    age = Column(Integer, primary_key=True)
    gender = Column(String, primary_key=True)
    height = Column(Float)
    weight = Column(Float)

    bmi = Column(Float, Computed("weight / (height * height)"))

    @property
    def verdict(self) -> str:
        if self.bmi is None:
            return None
        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi < 25:
            return "normal"
        elif self.bmi < 30:
            return "overweight"
        else:
            return "obese"
