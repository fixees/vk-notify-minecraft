from ping3 import ping, verbose_ping

from requests import get
from vkbottle.bot import BotLabeler, Message

main_labeler = BotLabeler()
main_labeler.vbml_ignore_case = True

@main_labeler.message(text="ты тут?")
async def check_me(message: Message):

    my_ip = get('https://api.ipify.org').content.decode('utf8')
    print(ping(my_ip))

    await message.reply('Я здесь!')






