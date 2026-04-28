from fastapi import APIRouter, Depends, Form, File, UploadFile
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.schemas.event import EventResponse
from app.schemas.rsvp import RSVPResponse
from app.services import event as event_service
from app.services import rsvp as rsvp_service

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("/", response_model=EventResponse)
def create_event(
    title: str = Form(...),
    description: str = Form(...),
    date: str = Form(...),
    location: str = Form(...),
    flyer: UploadFile | None = File(None),
    db: Session = Depends(get_db),
):
    """Create a new event."""
    return event_service.create_event(
        db=db,
        title=title,
        description=description,
        date=date,
        location=location,
        flyer=flyer,
    )


@router.get("/", response_model=list[EventResponse])
def list_events(db: Session = Depends(get_db)):
    """List all events."""
    return event_service.get_all_events(db)


@router.post("/{event_id}/rsvp", response_model=RSVPResponse)
def rsvp_to_event(
    event_id: int,
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(get_db),
):
    """RSVP to an event."""
    return rsvp_service.create_rsvp(db=db, event_id=event_id, name=name, email=email)


@router.get("/{event_id}/rsvps", response_model=list[RSVPResponse])
def get_event_rsvps(event_id: int, db: Session = Depends(get_db)):
    """Get list of RSVPs for an event."""
    return rsvp_service.get_rsvps_for_event(db=db, event_id=event_id)
