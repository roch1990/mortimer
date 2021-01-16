from sqlalchemy import Column, Integer, String, DateTime, JSON
from sqlalchemy.orm import relationship

from src.database import Base


class PostMortem(Base):
    __tablename__ = 'post_mortems'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    start_timestamp = Column(DateTime)
    end_timestamp = Column(DateTime)
    description = Column(String)
    steps = Column(JSON)

    users = relationship('User', backref='post_mortems', lazy=True)

    def __repr__(self):
        return f'{self.title}'
