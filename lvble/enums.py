from enum import Enum


class PortalEnum(str, Enum):
    CLICK_PAY = "click_pay"
    ACTIVE_BUILDING = "active_building"
    RENT_CAFE = "rent_cafe"


class PropertyEnum(str, Enum):
    OCEAN_PRIME = "Ocean Prime"
    GREY_STAR = "Grey Star"


class MethodEnum(str, Enum):
    POST = "POST"
    GET = "GET"
    DELETE = "DELETE"
    PUT = "PUT"
