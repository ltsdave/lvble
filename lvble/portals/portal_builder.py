from lvble.schemas import PortalEnum, UserInput

from .click_pay import ClickPay


class PortalException(Exception): ...


class ProtalBuilder:
    def __init__(self, user_input: UserInput):
        self.user_input = user_input

    def __call__(self):
        if self.user_input.portal == PortalEnum.CLICK_PAY:
            return ClickPay(self.user_input.username, self.user_input.password)
        elif self.user_input.portal == PortalEnum.ACTIVE_BUILDING:
            raise NotImplementedError(f"portal {PortalEnum.ACTIVE_BUILDING} not implemented yet")
        elif self.user_input.portal == PortalEnum.RENT_CAFE:
            raise NotImplementedError(f"portal {PortalEnum.RENT_CAFE} not implemented yet")
        else:
            raise PortalException(f"portal {self.user_input.portal} currently not supporteds")
