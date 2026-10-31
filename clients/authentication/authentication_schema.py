from pydantic import BaseModel, Field


# Добавили суффикс Schema вместо Dict
class TokenSchema(BaseModel):
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias="tokenType")  # Использовали alise
    access_token: str = Field(alias="accessToken")  # Использовали alise
    refresh_token: str = Field(alias="refreshToken")  # Использовали alise


# Добавили суффикс Schema вместо Dict
class LoginRequestSchema(BaseModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


# Добавили суффикс Schema вместо Dict
class LoginResponseSchema(BaseModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


# Добавили суффикс Schema вместо Dict
class RefreshRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias="refreshToken")  # Использовали alise
