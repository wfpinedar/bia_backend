from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.crud_base import CRUDBase
from app.models.meter import Meter
from app.schemas.meter import MeterCreate, MeterUpdate

class CRUDMeter(CRUDBase[Meter, MeterCreate, MeterUpdate]):
    # def create_with_owner(
    #     self, db: Session, *, obj_in: ItemCreate, owner_id: int
    # ) -> Item:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data, owner_id=owner_id)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    def get_daily(
        self, db: Session, *, meter_id: int, skip: int = 0, limit: int = 100
    ) -> List[Meter]:
        return (
            db.query(self.model)
            .filter(Meter.owner_id == meter_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


meter = CRUDMeter(Meter)