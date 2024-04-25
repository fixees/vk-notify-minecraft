# -*- coding: utf-8 -*-

from vkbottle import Bot
from settings import api, state_dispenser, labeler
from brain import main_labeler

labeler.load(main_labeler)

bot = Bot(
    api=api,
    labeler=labeler,
    state_dispenser=state_dispenser,
)

# Start
bot.run_forever()
