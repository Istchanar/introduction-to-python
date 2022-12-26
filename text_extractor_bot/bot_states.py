from aiogram.dispatcher.filters.state import State, StatesGroup

class BotStates(StatesGroup):
    weather = State()
    youtube = State()
    save_file = State()
