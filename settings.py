from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler

# ====================
# Настройки \ Settings
# ====================
token = "vk1.a.78lYeTp3f733xIGVzIFqD3tFYlreSJKALsk7-glMDs9OyV_5_yu3uVoU_V7MaxyTyxUVr6RKTa8rh3P_V1gMU250spNYCQXfHgchfJk-uHM5ro4JNag_bdOpEVIQw4BxBsZuuk0qghwxa3M0NWRXH1rX7kl4XXxnawyWX6XlQtLcAacATjJ8vMDtUpHqPeVbz0sX9rukxntWGbedltg0JQ"

who_notify = [319990365]  # ID кого уведомить (через запятую)
servers = []  # Пример заполнения: servers = ['fixees.ru', 36.36.36.36]

api = API(token)
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()
