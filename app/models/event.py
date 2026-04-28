from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.db import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    date = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    flyer_filename = Column(String(255), nullable=True)

    rsvps = relationship("RSVP", back_populates="event", cascade="all, delete-orphan")
