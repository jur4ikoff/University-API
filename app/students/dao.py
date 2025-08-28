
from app.dao.base import BaseDao
from app.students.models import Student


class StudentDao(BaseDao):
    model = Student