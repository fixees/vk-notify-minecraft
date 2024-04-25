from ping3 import ping, verbose_ping

import settings
from settings import who_notify, set_time_checking, servers


def get_peoples_notify():
    return who_notify


def get_set_time_checking():
    return set_time_checking


def get_servers():
    return servers

def check_address(ip: str):
    t_out = 5  # default 4
    output_unit = 'ms'  # 'ms', 's'

    if ping(ip, unit=output_unit, timeout=t_out) is False:
        return 'Error'
    elif ping(ip, unit=output_unit, timeout=t_out) is None:
        return 'Timeout'
    else:
        return '%.2f' % ping(ip, unit=output_unit, timeout=t_out) + output_unit