from sqlalchemy.orm import Session
import models, schema

def get_patient(db: Session):
    return db.query(models.Patient_db).all()

def get_patient_specific(db: Session, pat_id: int):
    return db.query(models.Patient_db).filter(models.Patient_db.id == pat_id).first()

def create_patient(db: Session, patient: schema.PatientCreate):
    db_pat = models.Patient_db(
        name=patient.name,
        email=patient.email,
        age=patient.age,
        gender=patient.gender,
        address=patient.address,
        height=patient.height,
        weight=patient.weight
    )
    db.add(db_pat)
    db.commit()
    db.refresh(db_pat)
    return db_pat

def update_pat(db: Session, pat_id: int, update_data: schema.PatientUpdate):
    pat = db.query(models.Patient_db).filter(models.Patient_db.id == pat_id).first()
    if not pat:
        return None

    data = update_data.model_dump(exclude_unset=True)
    for key, value in data.items():
        if value is not None:  
            setattr(pat, key, value)

    db.commit()
    db.refresh(pat)
    return pat

def del_pat(db: Session, pat_id: int):
    pat = db.query(models.Patient_db).filter(models.Patient_db.id == pat_id).first()
    if not pat:
        return None

    db.delete(pat)
    db.commit()
    return pat