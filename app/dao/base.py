from sqlalchemy.future import select
from app.database import async_session_maker
from app.students.models import Student

class BaseDao:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter(**filter_by)
            students = await session.execute(query)
            return students.scalars().all()