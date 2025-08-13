from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import Response, JSONResponse
import os
from typing import Optional
from sqlalchemy import select
from app.database import async_sesion_maker
from app.students.models import  Student, RBStudent, SUpdateFilter, StudentUpdate, SDeleteFilter




script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
path_to_json = os.path.join(parent_dir, "students.json")

app = FastAPI()


@app.get("/")
def root():
    return JSONResponse({"message": "Hello world"})


@app.get("/students")
def get_all_students():
    pass
    # students = json_to_dict_list()
    # return JSONResponse(students)


@app.get("/students/{course}")
def get_all_students_course(request_body: RBStudent = Depends()) -> list[Student]:
    pass
    # students = json_to_dict_list()

    # filtered_students = []

    # for student in students:
    #     if student["course"] == request_body.course:
    #         filtered_students.append(student)

    # if request_body.major:
    #     filtered_students = [student for student in filtered_students if student["major"].lower(
    #     ) == request_body.major.lower()]

    # if request_body.enrollment_year:
    #     filtered_students = [
    #         student for student in filtered_students if student["enrollment_year"] == request_body.enrollment_year]

    # return filtered_students


@app.get("/student", response_model=Student)
def get_student_by_id(student_id: int):
    pass
    # students = json_to_dict_list()
    # for student in students:
    #     if student["student_id"] == student_id:
    #         return student


@app.post("/add_student")
def add_student_handler(student: Student):
    pass
    # student_dict = student.dict()
    # check = add_student(student_dict)

    # if check:
    #     return JSONResponse({"message": "Студент успешно добавлен"})
    # else:
    #     return JSONResponse({"message": "Ошибка про добавлении студента"})


@app.put("/update_student")
def update_student_handler(filter_sudent: SUpdateFilter, new_data: StudentUpdate):
    pass
    # check = upd_student(filter_sudent.dict(), new_data.dict())

    # if check:
    #     return JSONResponse({"message" : "Информация успешно обновлена!"})
    # else:
    #     raise HTTPException(status_code=4000, detail="Ошика при обновлении информации о студенте")
    
@app.delete("/delete_student")
def delete_student_handler(filter_student: SDeleteFilter):
    pass
    # check = dell_student(filter_student.key, filter_student.value)

    # if check:
    #     return JSONResponse({"message" : "Студент успешно удален"} )
    # else:
    #     raise HTTPException(status_code=400, detail="Ошибка при удалении")