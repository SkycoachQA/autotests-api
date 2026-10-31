from pydantic import BaseModel, ConfigDict, Field

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class CourseSchema(BaseModel):
    """Курс с вложенными файлом превью и автором."""

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")
    preview_file: FileSchema = Field(alias="previewFile")
    created_by_user: UserSchema = Field(alias="createdByUser")


class GetCoursesQuerySchema(BaseModel):
    """Query списка курсов пользователя."""

    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class CreateCourseRequestSchema(BaseModel):
    """JSON создания курса с существующими previewFileId/createdByUserId."""

    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int | None = Field(alias="maxScore")
    min_score: int | None = Field(alias="minScore")
    description: str
    estimated_time: str | None = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class CreateCourseResponseSchema(BaseModel):
    """Ответ создания курса."""

    model_config = ConfigDict(populate_by_name=True)

    course: CourseSchema


class UpdateCourseRequestSchema(BaseModel):
    """Поля PATCH курса; пропущенные поля не отправляются клиентом."""

    model_config = ConfigDict(populate_by_name=True)

    title: str | None = None
    max_score: int | None = Field(alias="maxScore", default=None)
    min_score: int | None = Field(alias="minScore", default=None)
    description: str | None = None
    estimated_time: str | None = Field(alias="estimatedTime", default=None)
