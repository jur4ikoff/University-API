
from app.dao.base import BaseDAO
from app.students.models import Student
from app.database import async_session_maker

from sqlalchemy.orm import joinedload
from sqlalchemy.future import select
from sqlalchemy import insert, update, delete


class StudentDAO(BaseDAO):
    model = Student

    @classmethod
    async def find_full_data(cls, student_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).options(joinedload(
                cls.model.major)).filter_by(id=student_id)
            
            result = await session.execute(query)

            student_info = result.scalar_one_or_none()

            if not student_info:
                return None

            print(student_info)
            student_data = student_info.to_dict()
            student_data["major"] = student_info.major.major_name
            return student_data
