import os
import uuid

from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session

from app.repositories import event as event_repo
from app.schemas.event import EventResponse

UPLOAD_DIR = "uploads"


def _save_flyer(flyer: UploadFile) -> str:
    """Save the uploaded flyer file and return the stored filename."""
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    ext = os.path.splitext(flyer.filename)[1]
    filename = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(flyer.file.read())
    return filename


def _event_to_response(event) -> dict:
    """Convert an Event ORM object to a response-friendly dict, with rsvps as List[str]."""
    return {
        "id": event.id,
        "title": event.title,
        "description": event.description,
        "date": event.date,
        "location": event.location,
        "flyer_filename": event.flyer_filename,
        "rsvps": [rsvp.email for rsvp in event.rsvps],
    }


def create_event(
    db: Session,
    title: str,
    description: str,
    date: str,
    location: str,
    flyer: UploadFile | None = None,
) -> EventResponse:
    """Create a new event, optionally saving a flyer image."""
    flyer_filename = None
    if flyer and flyer.filename:
        flyer_filename = _save_flyer(flyer)

    event = event_repo.create_event(
        db=db,
        title=title,
        description=description,
        date=date,
        location=location,
        flyer_filename=flyer_filename,
    )
    return EventResponse(**_event_to_response(event))


def get_all_events(db: Session) -> list[EventResponse]:
    """Return all events."""
    events = event_repo.get_all_events(db)
    return [EventResponse(**_event_to_response(e)) for e in events]


def get_event(db: Session, event_id: int):
    """Fetch an event by ID or raise 404."""
    event = event_repo.get_event_by_id(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
