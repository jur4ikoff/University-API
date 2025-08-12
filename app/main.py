from fastapi import FastAPI
from fastapi.responses import Response, JSONResponse
import os
from typing import Optional

from utils import json_to_dict_list
from models import Student


script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, "students.json")

app = FastAPI()


@app.get("/")
def root():
    return JSONResponse({"message": "Hello world"})


@app.get("/students")
def get_all_students():
    students = json_to_dict_list(path_to_json)
    return JSONResponse(students)


@app.get("/students/{course}")
def get_all_students_course(course: int, major: Optional[str] = None, enrollment_year: Optional[int] = 2018) -> list[Student]:
    students = json_to_dict_list(path_to_json)

    filtered_students = []
    for student in students:
        if student["course"] == course:
            filtered_students.append(student)

    if major:
        filtered_students = [
            student for student in filtered_students if student["major"].lower() == major.lower()]

    if enrollment_year:
        filtered_students = [
            student for student in filtered_students if student["enrollment_year"] == enrollment_year]

    return filtered_students


@app.get("/student", response_model=Student)
def get_student_by_id(student_id: int):
    students = json_to_dict_list(path_to_json)
    for student in students:
        if student["student_id"] == student_id:
            return student
        
