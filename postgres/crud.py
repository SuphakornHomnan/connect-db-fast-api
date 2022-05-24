from sqlalchemy.orm import Session
from model import Person
from schemas import PersonSchema


def getPerson(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Person).offset(skip).limit(limit).all()


def getPersonById(db: Session, personId: str):
    return db.query(Person).filter(Person.id == int(personId)).first()


def createPerson(db: Session, person: PersonSchema):
    _person = Person(name=person.name, age=person.age, sex=person.sex)
    db.add(_person)
    db.commit()
    db.refresh(_person)
    return _person


def removePerson(db: Session, personId: str):
    _person = getPersonById(db=db, personId=personId)
    db.delete(_person)
    db.commit()


def updatePerson(db: Session, personId: str, name: str, age: int, sex: str):
    _person = getPersonById(db=db, personId=personId)

    if name:
        _person.name = name
    if age:
        _person.age = age
    if sex:
        _person.sex = sex

    db.commit()
    db.refresh(_person)
    return _person
