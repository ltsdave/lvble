import lvble.schemas as schemas
from lvble.enums import PropertyEnum
from lvble.portals.request_data import MethodEnum, RequestData

from .portal import Portal


class ClickPay(Portal):
    def __init__(self, username: str, password: str):
        super().__init__(username, password)
        self.requests_data = [
            RequestData(
                name="login",
                method=MethodEnum.POST,
                url="https://www.clickpay.com/MobileService/Service.asmx/login",
                data={
                    "username": self.username,
                    "password": self.password,
                    "validateUsername": True,
                },
            ),
            RequestData(
                name="user_info",
                method=MethodEnum.POST,
                url="https://www.clickpay.com/MobileService/Service.asmx/getUserContextJSON",
                data="NovelPayApp",
            ),
        ]

    def get_data(self) -> schemas.Tenant:
        for request in self.requests_data:
            self.responses[request.name] = request.execute(self.session)
        return self._extract_data_from_response()

    def _extract_data_from_response(self) -> schemas.Tenant:
        email = self.responses["user_info"]["Result"]["user"]["Email"]
        phone = self.responses["user_info"]["Result"]["user"]["Cellphone"]
        output_model = schemas.Tenant(
            email=email, phone=phone, property_company=PropertyEnum.OCEAN_PRIME, address="asdf"
        )
        return output_model
