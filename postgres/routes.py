from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import PersonSchema, Request, Response, IPerson, IUpdatePerson

import crud

router = APIRouter()


def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def creatPerson(request: IPerson, db: Session = Depends(getDb)):
    crud.createPerson(db, person=request)
    return Response(status="Created",
                    code="201",
                    message="Person created successfully").dict(exclude_none=True)


@router.get("/")
async def getPeople(skip: int = 0, limit: int = 100, db: Session = Depends(getDb)):
    _persons = crud.getPerson(db, skip, limit)
    return Response(status="Ok", code="200", message="Success fetch all data", result=_persons)


@router.patch("/update/{id}")
async def updatePerson(id: str, request: IUpdatePerson, db: Session = Depends(getDb)):
    _person = crud.updatePerson(db, personId=id,
                                name=request.name, age=request.age, sex=request.sex)
    return Response(status="No Content", code="204", message="Success update data", result=_person)


@router.delete("/delete/{id}")
async def deletePerson(id: str,  db: Session = Depends(getDb)):
    crud.removePerson(db, personId=id)
    return Response(status="Ok", code="200", message="Success delete data").dict(exclude_none=True)
