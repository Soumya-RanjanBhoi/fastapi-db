from fastapi import FastAPI, HTTPException, Depends
from fastapi.exceptions import RequestValidationError
from sqlalchemy.orm import Session
from database import engine, sessionlocal, Base
from typing import List
import models, schema, crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_patient", response_model=schema.PatientOut)
def create_apt(pat: schema.PatientCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_patient(db, pat)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating patient: {str(e)}")

@app.get("/all_patient", response_model=List[schema.PatientOut])
def get_all_data(db: Session = Depends(get_db)):
    return crud.get_patient(db)

@app.get("/get_patient/{pat_id}", response_model=schema.PatientOut)
def get_pat_detail(pat_id: int, db: Session = Depends(get_db)):
    pat = crud.get_patient_specific(db, pat_id)
    if not pat:
        raise HTTPException(status_code=404, detail="Patient not found")
    return pat

@app.put("/patient/{pat_id}", response_model=schema.PatientOut)
def update_detail(pat_id: int, updated_detail: schema.PatientUpdate, db: Session = Depends(get_db)):
    try:
        emp = crud.update_pat(db, pat_id, updated_detail)
        if not emp:
            raise HTTPException(status_code=404, detail="Patient not found")
        return emp
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error updating patient: {str(e)}")

@app.delete("/patient/{pat_id}", response_model=dict)
def del_patient(pat_id: int, db: Session = Depends(get_db)):
    pat = crud.del_pat(db, pat_id)
    if not pat:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"detail": "Patient deleted successfully"}