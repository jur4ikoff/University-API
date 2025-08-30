from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from app.config import get_auth_data
from app.users.dao import UsersDAO
from app.users.auth import get_token
from app.users.models import User

from fastapi import APIRouter, HTTPException, status, Depends

async def get_current_user(token: str = Depends(get_token)):
    try:
        auth_data = get_auth_data()
        payload = jwt.decode(token, auth_data["secret_key"], algorithms=[
                             auth_data['algorithm']])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, status="Токен не валидный!")

    # Проверяем срок действия токена
    expire = payload.get('exp')
    expire_time = datetime.fromtimestamp(int(expire), tz=timezone.utc)

    if (not expire) or (expire_time < datetime.now(timezone.utc)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Токен не валидный")

    # Проверяем, если ли параметр ID пользователя
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Не найден ID пользователя")
    
    # Ищем пользователя в базе данных
    user = await UsersDAO.find_one_none_by_id(int(user_id))
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user


async def get_current_admin_user(current_user: User = Depends(get_current_user)):
    if current_user.is_admin:
        return current_user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Недостатчоно прав")