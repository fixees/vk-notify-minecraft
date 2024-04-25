from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler

# ====================
# Настройки \ Settings
# ====================
token = ""

who_notify = [319990365]  # ID кого уведомить (через запятую)
servers = []  # Пример заполнения: servers = ['fixees.ru', 36.36.36.36]

api = API(token)
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()
