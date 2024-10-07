from abc import ABC, abstractmethod

import requests


class Portal(ABC):
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.responses: dict[str, dict] = {}

    @abstractmethod
    def get_data(self):
        raise NotImplementedError
