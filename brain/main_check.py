from requests import get
from vkbottle.bot import BotLabeler, Message

import functions

main_labeler = BotLabeler()
main_labeler.vbml_ignore_case = True


@main_labeler.message(text="?")
async def check_me(message: Message):

    my_ip = get('https://api.ipify.org').content.decode('utf8')

    answer = '''

myIP: {0} | {1}
    
    '''.format(
        my_ip, functions.check_address(my_ip)

    )

    await message.reply(answer)
