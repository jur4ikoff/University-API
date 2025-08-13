import requests
from pydantic import ValidationError
from datetime import date, datetime

from models import Student


def get_all_students():
    url = "http://127.0.0.1:8000/students/2"
    response = requests.get(url)
    print(response.status_code)  # Убедитесь, что статус 200
    print(response.text)


def test_valid_student(data: dict) -> None:
    try:
        student = Student(**data)
        print(student)
    except ValidationError as e:
        print(f"Ошибка валидации: {e}")


student_data = {
    "student_id": 1,
    "phone_number": "+1234567890",
    "first_name": "Иван",
    "last_name": "Иванов",
    "date_of_birth": date(2000, 1, 1),
    "email": "ivan.ivanov@example.com",
    "address": "Москва, ул. Пушкина, д. Колотушкина",
    "enrollment_year": 2022,
    "major": "Информатика",
    "course": 3,
    "special_notes": "Увлекается программированием"
}

print(test_valid_student(student_data))
