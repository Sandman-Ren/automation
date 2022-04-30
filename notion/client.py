NOTION_BASE_URL = r'https://api.notion.com'

import json
from json import JSONEncoder

class Client:
    def __init__(self, bearer_token: str):
        self.bearer_token = bearer_token
