"""Pydantic-модели запроса и ответа POST /api/v1/users."""

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """Данные пользователя в API: идентификатор, email и три имени."""

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Запрос создания пользователя: email, пароль и имена в формате API."""

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """Ответ создания пользователя с вложенным объектом UserSchema."""

    user: UserSchema
