from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler

# Настройки \ Settings
token = "vk1.a.78lYeTp3f733xIGVzIFqD3tFYlreSJKALsk7-glMDs9OyV_5_yu3uVoU_V7MaxyTyxUVr6RKTa8rh3P_V1gMU250spNYCQXfHgchfJk-uHM5ro4JNag_bdOpEVIQw4BxBsZuuk0qghwxa3M0NWRXH1rX7kl4XXxnawyWX6XlQtLcAacATjJ8vMDtUpHqPeVbz0sX9rukxntWGbedltg0JQ"

set_time_checking = 0  # (от 0 сек. до 10 сек.)

servers = {                 # Создание серверов для пинга.
    "1.1.1.1": "tcp",       # Доступно 2 протокола: tcp, http
    "fixees.ru": "http",    # Пример http сервера выглядит так - "fixees.ru": "http"
}

api = API(token)
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()
