from sqlalchemy.orm import Session

from lvble import schemas
from lvble.db import models


def get_by_email(db: Session, email: str) -> models.Tenant:
    return db.query(models.Tenant).filter(models.Tenant.email == email).first()


def get_all(db: Session) -> list[models.Tenant]:
    return db.query(models.Tenant).all()


def create(db: Session, tenant: schemas.Tenant) -> models.Tenant:
    tenant = models.Tenant(**tenant.model_dump())
    db.add(tenant)
    db.commit()
    db.refresh(tenant)
    return tenant
