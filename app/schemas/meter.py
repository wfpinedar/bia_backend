from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field


# Shared properties
class MeterBase(BaseModel):
    id: int = Field(None, description="ID")
    meter_id: Optional[int] = Field(None, description="Id of meter machine")
    meter_date: Optional[datetime] = Field(None, description="Sample Datetime")
    active_energy: float = Field(None, description="Active Energy")


# Properties to receive on item creation
class MeterCreate(MeterBase):
    pass

# Properties to receive on item update
class MeterUpdate(MeterBase):
    pass


# Properties shared by models stored in DB
class MeterInDBBase(MeterBase):
    id: int
    meter_id: int
    meter_date: datetime
    active_energy: float

    class Config:
        orm_mode = True


# Properties to return to client
class Meter(MeterInDBBase):
    pass


# Properties properties stored in DB
class MeterInDB(MeterInDBBase):
    pass

class Usage(BaseModel):
    meter_date: datetime
    value: float