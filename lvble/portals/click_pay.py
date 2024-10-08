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
            RequestData(
                name="unit_info",
                method=MethodEnum.POST,
                url="https://www.clickpay.com/MobileService/Service.asmx/get_data_allow_impersonation_json",
                data={"RequestType": "get_user_paynow_desktop", "FilterByGroupLabel": "1", "GroupLabel": ""},
            ),
        ]

    def get_data(self) -> schemas.Tenant:
        for request in self.requests_data:
            self.responses[request.name] = request.execute(self.session)
        return self._extract_data_from_response()

    def _extract_data_from_response(self) -> schemas.Tenant:
        email = self.responses["user_info"]["Result"]["user"]["Email"]
        phone = self.responses["user_info"]["Result"]["user"]["Cellphone"]
        property_company = self.responses["unit_info"]["Result"]["Unit"]["Unit"]["SiteName"]
        address = self._extract_address()
        output_model = schemas.Tenant(
            email=email, phone=phone, property_company=property_company, address=address
        )
        return output_model

    def _extract_address(self) -> str:
        unit_info = self.responses["unit_info"]["Result"]["Unit"]["Unit"]
        street_name = unit_info["StreetName"]
        street_number = unit_info["StreetNumber"]
        apt_number = unit_info["AptNumber"]
        city = unit_info["City"]
        state = unit_info["State"]
        zip = unit_info["Zip"]
        return f"{street_number} {street_name} {apt_number}, {city} {state} {zip}"
