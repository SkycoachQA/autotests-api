from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """JSON создания пользователя: все пять строковых полей обязательны."""

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """Клиент публичных методов /api/v1/users, не требующих авторизации."""

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """Создаёт пользователя POST-запросом к /api/v1/users.

        :param request: JSON-словарь с email, password, lastName, firstName, middleName.
        :return: httpx.Response; при успехе JSON с данными созданного user.
        """
        return self.post("/api/v1/users", json=request)
