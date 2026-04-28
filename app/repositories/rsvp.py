from sqlalchemy.orm import Session

from app.models.rsvp import RSVP


def create_rsvp(db: Session, event_id: int, name: str, email: str) -> RSVP:
    """Insert a new RSVP for a given event."""
    rsvp = RSVP(name=name, email=email, event_id=event_id)
    db.add(rsvp)
    db.commit()
    db.refresh(rsvp)
    return rsvp


def get_rsvps_by_event(db: Session, event_id: int) -> list[RSVP]:
    """Return all RSVPs for a specific event."""
    return db.query(RSVP).filter(RSVP.event_id == event_id).all()
