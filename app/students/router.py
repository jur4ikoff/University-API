
from fastapi import APIRouter
from sqlalchemy import select
from app.database import async_sesion_maker
from app.students.models import Student


router = APIRouter(prefix="/students", tags=["Работа со студентами"])


@router.get("/", summary="Получить всех студентов")
async def get_all_students():
    print(1)
    # Создаем ассинхроннную сессию
    async with async_sesion_maker() as session:
        
        # Создаем запрос
        query = select(Student)

        # Выполнение запроса
        result = await session.execute(query)

        # # Извлекаем результат
        # students = result.scalar().all()

        # return students