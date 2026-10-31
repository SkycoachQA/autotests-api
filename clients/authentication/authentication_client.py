from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class LoginRequestDict(TypedDict):
    """JSON входа: обязательные строковые email и password."""

    email: str
    password: str


class RefreshRequestDict(TypedDict):
    """JSON обновления: обязательный строковый refreshToken из ответа login."""

    refreshToken: str


class AuthenticationClient(APIClient):
    """Клиент методов /api/v1/authentication."""

    def login_api(self, request: LoginRequestDict) -> Response:
        """Выполняет вход.

        :param request: JSON-словарь с email и password.
        :return: httpx.Response с результатом запроса login.
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """Запрашивает обновление токенов.

        :param request: JSON-словарь с refreshToken.
        :return: httpx.Response с результатом запроса refresh.
        """
        return self.post("/api/v1/authentication/refresh", json=request)
