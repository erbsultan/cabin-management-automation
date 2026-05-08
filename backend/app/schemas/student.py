from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class StudentCreate(BaseModel):
    login: str = Field(min_length=2, max_length=50)
    full_name: str | None = Field(default=None, max_length=150)


class StudentRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    login: str
    full_name: str | None
    base_trust_score: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

