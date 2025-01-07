from api.core import CoreSearchApi


class AskBot:
    @classmethod
    def search_ask(self, question: str):
        if not question:
            return 'Como posso ajudar?'
        data = {'query': question, 'provedor_ai': 'groq'}
        print(data)

        resp = CoreSearchApi.request_bot(data)

        return resp.json().get('response')
