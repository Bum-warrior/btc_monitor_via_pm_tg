import requests
import time
from cfg import token, admin_id
import json

url = "https://api.telegram.org/bot{0}/sendMessage".format(token)
url2 = "https://api.telegram.org/bot{0}/sendPhoto".format(token)
url3 = "https://api.telegram.org/bot{0}/sendMediaGroup".format(token)


def message_user(message_text: str, chat_id: int):
    '''
    Send message to user
    :param message_text:
    :param chat_id:
    :return:
    '''
    message_data = {
        'chat_id': chat_id,
        'text': message_text,
        'parse_mode': 'HTML'
    }
    requests.post(url, data=message_data)


def send_photo(chat_id, photo, caption='', parse_mode=None, disable_notification=False, reply_to_message_id=0,
               reply_markup=None):
    with open(photo, 'rb') as file:
        response = requests.post(
            'https://api.telegram.org/bot{token}/sendPhoto?'.format(token=token),
            data={
                'chat_id': chat_id,  # Integer or String
                'caption': caption,  # String
                'parse_mode': parse_mode,  # String https://core.telegram.org/bots/api#formatting-options
                'disable_notification': disable_notification,  # Boolean
                'reply_to_message_id': reply_to_message_id,  # Integer
                'reply_markup': json.dumps(reply_markup) if reply_markup is not None else reply_markup,  # List
            },
            files={
                'photo': file.read(),
            }
        )
        file.close()
        if response.status_code == 200:
            return json.loads(response.text)




if __name__ == '__main__':
    pass
