from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetExercisesQueryDict(TypedDict):
    """Query-параметры списка заданий: идентификатор курса courseId."""

    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """JSON создания задания; nullable-поля и orderIndex задаются явно по курсу."""

    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class UpdateExerciseRequestDict(TypedDict):
    """JSON обновления задания; значения допускают None, ключи заданы явно."""

    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class Exercise(TypedDict):
    """JSON упражнения, включая идентификатор курса и nullable-поля баллов/времени."""

    id: str
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None


class GetExerciseResponseDict(TypedDict):
    """Ответ получения одного упражнения."""

    exercise: Exercise


class GetExercisesResponseDict(TypedDict):
    """Ответ списка упражнений курса."""

    exercises: list[Exercise]


class CreateExerciseResponseDict(TypedDict):
    """Ответ создания упражнения."""

    exercise: Exercise


class UpdateExerciseResponseDict(TypedDict):
    """Ответ обновления упражнения."""

    exercise: Exercise


class ExercisesClient(APIClient):
    """Клиент методов /api/v1/exercises, использующий настроенный транспорт APIClient."""

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """Получает список заданий курса.

        :param query: Query-словарь с courseId.
        :return: httpx.Response с JSON-списком exercises при успехе.
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """Получает задание по идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: httpx.Response с JSON-объектом exercise при успехе.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """Создаёт задание в курсе POST-запросом.

        :param request: JSON с title, courseId, maxScore, minScore, orderIndex,
            description и estimatedTime.
        :return: httpx.Response с JSON созданного exercise при успехе.
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """Обновляет задание PATCH-запросом.

        :param exercise_id: Идентификатор обновляемого задания.
        :param request: JSON с title, maxScore, minScore, orderIndex,
            description и estimatedTime.
        :return: httpx.Response с JSON обновлённого exercise при успехе.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """Удаляет задание DELETE-запросом.

        :param exercise_id: Идентификатор удаляемого задания.
        :return: httpx.Response; тело зависит от контракта удаления сервера.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """Возвращает JSON получения упражнения exercise_id."""
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """Возвращает JSON списка упражнений по query с courseId."""
        response = self.get_exercises_api(query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """Создаёт упражнение из request и возвращает JSON ответа."""
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """Обновляет упражнение exercise_id данными request и возвращает JSON."""
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """Создаёт авторизованный клиент упражнений по email/password из user."""
    return ExercisesClient(client=get_private_http_client(user))
