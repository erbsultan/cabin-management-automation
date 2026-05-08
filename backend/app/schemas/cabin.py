from datetime import datetime

from pydantic import BaseModel, ConfigDict


class CabinRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number: int
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime
