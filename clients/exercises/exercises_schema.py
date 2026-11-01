from tools.fakers import fake

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

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias='courseId', default_factory=fake.uuid4)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int = Field(alias='orderIndex', default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


class UpdateExerciseRequestSchema(BaseModel):
    """Данные PATCH упражнения; незаданные поля генерируются для полного обновления."""

    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias='maxScore', default_factory=fake.max_score)
    min_score: int | None = Field(alias='minScore', default_factory=fake.min_score)
    order_index: int | None = Field(alias='orderIndex', default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias='estimatedTime', default_factory=fake.estimated_time)


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
