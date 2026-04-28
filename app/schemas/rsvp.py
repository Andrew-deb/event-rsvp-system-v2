from pydantic import BaseModel


class RSVPBase(BaseModel):
    """Schema matching the assignment's RSVP data model."""
    name: str
    email: str


class RSVPResponse(RSVPBase):
    id: int
    event_id: int

    class Config:
        from_attributes = True
