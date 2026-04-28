from pydantic import BaseModel
from typing import Optional, List


class EventBase(BaseModel):
    title: str
    description: str
    date: str
    location: str


class EventResponse(EventBase):
    """Response schema matching the assignment's Event data model."""
    id: int
    flyer_filename: Optional[str] = None
    rsvps: List[str] = []

    class Config:
        from_attributes = True
