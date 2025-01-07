import os

import requests
from dotenv import load_dotenv


class CoreSearchApi:
    @classmethod
    def request_bot(self, data: dict):
        session = requests.session()
        response = session.post(get_url(), json=data)
        if response.status_code != 200:  # noqa: PLR2004
            response.raise_for_status()
        return response


def get_url():  # noqa: PLR6301
    load_dotenv()
    if not os.getenv('URL_BASE'):
        raise ValueError('URL_BASE not found')

    return os.getenv('URL_BASE') + 'assistent/seach'
