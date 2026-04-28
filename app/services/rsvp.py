from sqlalchemy.orm import Session

from app.repositories import rsvp as rsvp_repo
from app.schemas.rsvp import RSVPResponse
from app.services.event import get_event


def create_rsvp(db: Session, event_id: int, name: str, email: str) -> RSVPResponse:
    """RSVP to an event. Validates that the event exists first."""
    get_event(db, event_id)
    rsvp = rsvp_repo.create_rsvp(db=db, event_id=event_id, name=name, email=email)
    return RSVPResponse.model_validate(rsvp)


def get_rsvps_for_event(db: Session, event_id: int) -> list[RSVPResponse]:
    """Get all RSVPs for a specific event."""
    get_event(db, event_id)
    rsvps = rsvp_repo.get_rsvps_by_event(db, event_id)
    return [RSVPResponse.model_validate(r) for r in rsvps]
