from sqlalchemy.orm import Session

from app.models.event import Event


def create_event(db: Session, title: str, description: str, date: str, location: str, flyer_filename: str | None = None) -> Event:
    """Insert a new event into the database."""
    event = Event(
        title=title,
        description=description,
        date=date,
        location=location,
        flyer_filename=flyer_filename,
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def get_all_events(db: Session) -> list[Event]:
    """Return all events."""
    return db.query(Event).all()


def get_event_by_id(db: Session, event_id: int) -> Event | None:
    """Return a single event by its ID, or None."""
    return db.query(Event).filter(Event.id == event_id).first()
