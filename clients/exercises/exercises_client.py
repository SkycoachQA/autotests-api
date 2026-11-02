from clients.api_coverage import tracker
from tools.routes import APIRoutes
import allure

from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, UpdateExerciseRequestSchema, GetExerciseResponseSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, UpdateExerciseResponseSchema

class ExercisesClient(APIClient):
    """Клиент методов /api/v1/exercises, использующий настроенный транспорт APIClient."""

    @allure.step('Get exercises')
    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """Получает список заданий курса.

        :param query: Query-словарь с courseId.
        :return: httpx.Response с JSON-списком exercises при успехе.
        """
        return self.get(APIRoutes.EXERCISES, params=query.model_dump(by_alias=True))

    @allure.step('Get exercise by id {exercise_id}')
    @tracker.track_coverage_httpx(f'{APIRoutes.EXERCISES}/{{exercise_id}}')
    def get_exercise_api(self, exercise_id: str) -> Response:
        """Получает задание по идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: httpx.Response с JSON-объектом exercise при успехе.
        """
        return self.get(f'{APIRoutes.EXERCISES}/{exercise_id}')

    @allure.step('Create exercise')
    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """Создаёт задание в курсе POST-запросом.

        :param request: JSON с title, courseId, maxScore, minScore, orderIndex,
            description и estimatedTime.
        :return: httpx.Response с JSON созданного exercise при успехе.
        """
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @allure.step('Update exercise by id {exercise_id}')
    @tracker.track_coverage_httpx(f'{APIRoutes.EXERCISES}/{{exercise_id}}')
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """Обновляет задание PATCH-запросом.

        :param exercise_id: Идентификатор обновляемого задания.
        :param request: JSON с title, maxScore, minScore, orderIndex,
            description и estimatedTime.
        :return: httpx.Response с JSON обновлённого exercise при успехе.
        """
        return self.patch(f'{APIRoutes.EXERCISES}/{exercise_id}', json=request.model_dump(by_alias=True, exclude_none=True))

    @allure.step('Delete exercise by id {exercise_id}')
    @tracker.track_coverage_httpx(f'{APIRoutes.EXERCISES}/{{exercise_id}}')
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """Удаляет задание DELETE-запросом.

        :param exercise_id: Идентификатор удаляемого задания.
        :return: httpx.Response; тело зависит от контракта удаления сервера.
        """
        return self.delete(f'{APIRoutes.EXERCISES}/{exercise_id}')

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """Возвращает проверенную Pydantic-модель получения упражнения exercise_id."""
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """Возвращает проверенную Pydantic-модель списка упражнений по query с courseId."""
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """Создаёт упражнение из request и возвращает проверенную модель ответа."""
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """Обновляет упражнение exercise_id данными request и возвращает модель ответа."""
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """Создаёт авторизованный ExercisesClient для переданного пользователя."""
    return ExercisesClient(client=get_private_http_client(user))
