import json

import requests
from pydantic import BaseModel

from lvble.enums import MethodEnum


class RequestData(BaseModel):
    name: str
    method: MethodEnum
    url: str
    data: dict | str | None

    def execute(self, session: requests.Session) -> dict:
        return json.loads(session.request(self.method, self.url, data=self.serelize_data()).text)

    def serelize_data(self) -> dict | str | None:
        if isinstance(self.data, str):
            return self.data
        elif isinstance(self.data, dict):
            return json.dumps(self.data)
