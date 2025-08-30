
from fastapi import APIRouter, Depends
from fastapi.responses import Response
from app.students.dao import StudentDAO
from app.students.rb import RBStudent
from app.students.schemas import SStudent, SStudentAdd

router = APIRouter(prefix="/students", tags=["Работа со студентами"])


@router.get("/", summary="Получить всех студентов")
async def get_all_students(request_body: RBStudent = Depends()) -> list[SStudent]:
    return await StudentDAO.find_all()


@router.get("/{id}", summary="Получить одного студента по id")
async def get_student_by_id(student_id: int) -> SStudent | dict:
    res = await StudentDAO.find_full_data(student_id)
    if res is None:
        return {"message": f"Студент с ID {student_id} не найден!"}

    return res


@router.get("/by_filter", summary="Получить одного студента по фильтру")
async def get_student_by_filter(request_body: RBStudent = Depends()) -> SStudent | dict:
    res = await StudentDAO.find_one_or_none(**request_body.to_dict())

    if res is None:
        return {"message": f"Студент с указанными вами параметрами не найден!"}

    return res


@router.post("/add/", summary="Добавить студента")
async def add_student(student: SStudentAdd) -> dict:
    check = await StudentDAO.add_student(**student.dict())

    if check:
        return {"message": "Студент успешно добавлен", "student": student}
    else:
        return {"message": "Ошибка при добавлении студента"}

@router.delete("/delete/{student_id}", summary="Удаление пользователя по ID")
async def delete_student_by_id(student_id: int) -> dict:
    check = await StudentDAO.delete_student_by_id(student_id=student_id)
    if check:
        return {"message": f"Студент с ID {student_id} удален!"}
    else:
        return {"message": "Ошибка при удалении студента"}
    