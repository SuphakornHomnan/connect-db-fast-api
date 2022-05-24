from typing import List, Optional, Generic, TypeVar, Union
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class PersonSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class IPerson(GenericModel):
    name: str
    age: int
    sex: str


class IUpdatePerson(GenericModel):
    name: Union[str, None]
    age: Union[int, None]
    sex: Union[str, None]


class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]
