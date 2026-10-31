from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


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
