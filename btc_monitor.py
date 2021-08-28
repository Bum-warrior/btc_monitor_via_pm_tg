import p_rate
import cfg
import broadcast
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)
last_rate = 0

if __name__ == '__main__':
    while True:
        rate_get = p_rate.get(cfg.btc_usd)
        string = str(rate_get[:6])
        rate = int(''.join(string.split()))
        diff = abs(rate - last_rate)
        logging.info(msg='Курс биткоина: ' + str(rate))
        if diff > 1000:
            broadcast.message_user(message_text=f"Курс биткоина: {rate}", chat_id=cfg.admin_id[0])
            last_rate = rate
        sleep(300)