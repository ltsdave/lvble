from enum import Enum

from pydantic import BaseModel

from lvble.enums import PortalEnum, PropertyEnum


class UserInput(BaseModel):
    portal: PortalEnum
    username: str
    password: str


class Tenant(BaseModel):
    address: str
    property_company: PropertyEnum
    email: str
    phone: str
