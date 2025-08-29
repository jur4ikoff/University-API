from pydantic import BaseModel, Field

class SMajorsAdd(BaseModel):
    major_name: str = Field(..., description="Название факультета")
    major_description: str = Field(None, description="Описание факульета")
    count_students: int = Field(0, descriptions="Количество студентов")

class SMajorsUpdDesc(BaseModel):
    major_name: str = Field(..., description="Название факультета")
    major_description: str = Field(None, description="Описание факультета")