# -*- coding: utf-8 -*-

from vkbottle import Bot

import functions
import sentences
from settings import api, state_dispenser, labeler
from brain import main_labeler

labeler.load(main_labeler)

bot = Bot(
    api=api,
    labeler=labeler,
    state_dispenser=state_dispenser,
)


@bot.loop_wrapper.interval(seconds=15)
async def repeated_task():
    servers = functions.get_servers()
    output = ''

    for server in servers:

        if functions.check_address(server) == 'Error':
            output += sentences.output_error.format(server)

        elif functions.check_address(server) == 'Timeout':
            output += sentences.output_timeout.format(server)

    if output != '':
        ids = functions.get_peoples_notify()

        for id in ids:

            try:
                await bot.api.messages.send(
                    peer_id=id,
                    message=sentences.notify_message + output,
                    random_id=0
                )
            except:
                continue
    else:

        print('20.12 19:22 | It`s okey')


# Start
bot.run_forever()
