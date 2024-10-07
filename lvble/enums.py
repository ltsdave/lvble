from enum import Enum


class PortalEnum(str, Enum):
    CLICK_PAY = "click_pay"
    ACTIVE_BUILDING = "active_building"
    RENT_CAFE = "rent_cafe"


class PropertyEnum(str, Enum):
    OCEAN_PRIME = "ocean prime"
    GREY_STAR = "grey star"


class MethodEnum(str, Enum):
    POST = "POST"
    GET = "GET"
