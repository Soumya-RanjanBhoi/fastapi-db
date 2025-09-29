from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,Optional,Literal

class patient_base(BaseModel):
    name: Annotated[str, Field(..., description="Name of the patient")]
    email:Annotated[EmailStr, Field(..., description="email of the patient")]
    address:Optional[str]= Field(None, description='Address of user')
    age: Annotated[int, Field(gt=0)]
    gender: Annotated[Literal['male', 'female', 'other'], Field(..., description='gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='height in meters', json_schema_extra={"example": 1.75})]
    weight: Annotated[float, Field(..., gt=0, description='weight in kg', json_schema_extra={"example": 70})]

class EmployeeCreate(patient_base):
    pass 

class EmployeeUpdate(patient_base):
    name: Optional[str] = None
    city: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[Literal['male', 'female', 'other']] = None
    height: Optional[float] = Field(default=None, gt=0)
    weight: Optional[float] = Field(default=None, gt=0)

class EmployeeOut(patient_base):
    id:int

    class Config:
        orm_mode=True

