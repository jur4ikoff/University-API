from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator, ValidationError
from datetime import date, datetime
from typing import Optional, Any
import re


class Major(str, Enum):
    informatics = "Информатика"
    economics = "Экономика"
    low = "Право"
    medicine = "Медицина"
    engenering = "Инженерия"
    languages = "Языки"
    history = "История"
    math = "Математика"
    biology = "Биология"


class RBStudent:
    def __init__(self, course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018):
        self.course: int = course
        self.major: Optional[str] = major
        self.enrollment_year: Optional[int] = enrollment_year

class SUpdateFilter(BaseModel):
    student_id: int

class SDeleteFilter(BaseModel):
    key: str
    value: Any

class StudentUpdate(BaseModel):
    course: int = Field(..., ge=1, le=5, description="Курс, от 1 до 5")
    major: Optional[Major] = Field(..., description="Специальность")

class Student(BaseModel):
    student_id: int
    phone_number: str = Field(default=..., description="Номер телефона с +")
    first_name: str = Field(default=..., min_length=1,
                            max_length=58, description="Имя студента")
    last_name: str = Field(default=..., min_length=1,
                           max_length=58, description="Фамилия студента")
    date_of_birth: date = Field(
        default=..., description="Дата рожления студента в формате от 1 до 50 символов")
    email: EmailStr = Field(default=..., description="Электронная почта")
    address: str = Field(default=..., min_length=1,
                         max_length=200, description="Адрес студента")
    enrollment_year: int = Field(default=..., description="год поступления")
    major: Major = Field(default=..., description="Специальность студента")
    course: int = Field(default=...,  ge=1, le=5,
                        description="Курс должен быть в диапазоне от 1 до 5")
    special_notes: Optional[str] = Field(
        default=None, max_length=600, description="Дополнительные заметки до 600 символов")


@field_validator("phone_number")
@classmethod
def validate_phone_number(cls, values: str) -> str:
    if not re.match(r'^\+\d{1,15}$', values):
        raise ValueError(
            'Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
    return values


@field_validator("date_of_birth")
@classmethod
def validate_date_of_birth(cls, values: date):
    if values and values >= datetime.now().date():
        raise ValueError('Дата рождения должна быть в прошлом')
    return values
