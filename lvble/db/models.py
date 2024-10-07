from sqlalchemy import Column, Enum, Integer, String

from lvble.schemas import PropertyEnum

from .database import Base


class Tenant(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True)
    email = Column(String, index=True, unique=True)
    property_company = Column(Enum(PropertyEnum))
    address = Column(String)
    phone = Column(String)
