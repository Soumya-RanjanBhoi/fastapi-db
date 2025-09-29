from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Optional, Literal

class PatientBase(BaseModel):
    name: Annotated[str, Field(..., description="Name of the patient")]
    email: Annotated[EmailStr, Field(..., description="Email of the patient")]
    address: Optional[str] = Field(None, description="Address of patient")
    age: Annotated[int, Field(gt=0)]
    gender: Annotated[Literal['male','female','other'], Field(...)]
    height: Annotated[float, Field(..., gt=0, description="Height in meters")]
    weight: Annotated[float, Field(..., gt=0, description="Weight in kg")]

class PatientCreate(PatientBase):
    pass

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    age: Optional[int] = Field(None, gt=0)
    gender: Optional[Literal['male','female','other']] = None
    height: Optional[float] = Field(None, gt=0, description="Height in meters")
    weight: Optional[float] = Field(None, gt=0, description="Weight in kg")

class PatientOut(PatientBase):
    id: int
    bmi: Optional[float] = None
    verdict: Optional[str] = None

    class Config:
        from_attributes = True 