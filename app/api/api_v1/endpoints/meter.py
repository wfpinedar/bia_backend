from typing import Any, List

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import and_

from app import crud, models, schemas
from app.schemas.meter import MeterCreate
from app.api import deps
from app.utils.time import get_periods
from app.utils.consumption import get_usages

router = APIRouter()



@router.get("/", response_model=List[schemas.meter.Meter])
def read_meters(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve meters.
    """
    meters = crud.meter.get_multi(db, skip=skip, limit=limit)
    return meters


@router.get("/usage", response_model=List[schemas.meter.Usage])
def read_meters(
    db: Session = Depends(deps.get_db),
    date: str = "2022-10-12",
    period: str = "daily",
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve meters.
    """
    periods = get_periods(date, period)
    meters = (db.query(models.meter.Meter) # TODO: add validation when periods come udefined
              .filter(
                  and_(
                    models.meter.Meter.meter_date.between(
                        periods[0], 
                        periods[-1]
                    )
                  )
                  )
              .all())
    usages = get_usages(meters, period)
    consumptions = [{"meter_date": key, "value": value} for key, value in usages.items()]
    print(consumptions)
    return consumptions #meters#get_usages(periods, meters)

    # meters = crud.meter.get_multi(db, skip=skip, limit=limit)
    # [print(meter) for meter in meters]
    # return meters

@router.post("/", response_model=schemas.meter.Meter)
def create_meter(
    *,
    db: Session = Depends(deps.get_db),
    meter_in: schemas.meter.MeterCreate,
) -> Any:
    """
    Create new meter.
    """
    meter = crud.meter.create(db=db, obj_in=meter_in)
    return meter


# @router.put("/{id}", response_model=schemas.Meter)
# def update_meter(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     meter_in: schemas.MeterUpdate,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Update an meter.
#     """
#     meter = crud.meter.get(db=db, id=id)
#     if not meter:
#         raise HTTPException(status_code=404, detail="Meter not found")
#     if not crud.user.is_superuser(current_user) and (meter.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     meter = crud.meter.update(db=db, db_obj=meter, obj_in=meter_in)
#     return meter


# @router.get("/{id}", response_model=schemas.Meter)
# def read_meter(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Get meter by ID.
#     """
#     meter = crud.meter.get(db=db, id=id)
#     if not meter:
#         raise HTTPException(status_code=404, detail="Meter not found")
#     if not crud.user.is_superuser(current_user) and (meter.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     return meter


# @router.delete("/{id}", response_model=schemas.Meter)
# def delete_meter(
#     *,
#     db: Session = Depends(deps.get_db),
#     id: int,
#     current_user: models.User = Depends(deps.get_current_active_user),
# ) -> Any:
#     """
#     Delete an meter.
#     """
#     meter = crud.meter.get(db=db, id=id)
#     if not meter:
#         raise HTTPException(status_code=404, detail="Meter not found")
#     if not crud.user.is_superuser(current_user) and (meter.owner_id != current_user.id):
#         raise HTTPException(status_code=400, detail="Not enough permissions")
#     meter = crud.meter.remove(db=db, id=id)
#     return meter