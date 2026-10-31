from pydantic import BaseModel, ConfigDict, Field

class ExerciseSchema(BaseModel):
    """Данные упражнения курса."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")


class GetExercisesQuerySchema(BaseModel):
    """Query списка упражнений курса."""

    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias="courseId")


class CreateExerciseRequestSchema(BaseModel):
    """JSON создания упражнения."""

    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """Поля PATCH упражнения; пропущенные поля не отправляются клиентом."""

    model_config = ConfigDict(populate_by_name=True)

    title: str | None = None
    max_score: int | None = Field(alias="maxScore", default=None)
    min_score: int | None = Field(alias="minScore", default=None)
    order_index: int | None = Field(alias="orderIndex", default=None)
    description: str | None = None
    estimated_time: str | None = Field(alias="estimatedTime", default=None)


class GetExerciseResponseSchema(BaseModel):
    """Ответ операции GetExercise."""

    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema


class GetExercisesResponseSchema(BaseModel):
    """Ответ операции GetExercises."""

    model_config = ConfigDict(populate_by_name=True)

    exercises: list[ExerciseSchema]


class CreateExerciseResponseSchema(BaseModel):
    """Ответ операции CreateExercise."""

    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema


class UpdateExerciseResponseSchema(BaseModel):
    """Ответ операции UpdateExercise."""

    model_config = ConfigDict(populate_by_name=True)

    exercise: ExerciseSchema
