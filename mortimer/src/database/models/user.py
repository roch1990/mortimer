from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    nickname = Column(String)
    hash = Column(String)

    post_mortem_id = Column(Integer, ForeignKey('post_mortems.id'))
    post_mortem = relationship("PostMortem", back_populates="users")

    def __repr__(self):
        return f'{self.nickname}'