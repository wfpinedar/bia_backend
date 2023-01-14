from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Meter(Base):
    __tablename__ = 'meter'
    
    id = Column(Integer, primary_key=True, index=True)
    meter_id = Column(Integer, index=True)
    meter_date = Column(DateTime, index=True)
    active_energy = Column(Float, index=True)
