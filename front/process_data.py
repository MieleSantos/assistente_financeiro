from api.search_bot import AskBot

bot = AskBot()


def select_model():
    model_options = [
        'gpt-3.5-turbo',
        'gpt-4',
        'gpt-4-turbo',
        'gpt-4o-mini',
        'gpt-4o',
    ]

    return model_options


def ask_question(model, query, st):
    return AskBot.search_ask(query)
