import random

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll


def send_message_in_chat(chat_id: int, message: str, vk_session: VkApi) -> None:
    vk = vk_session.get_api()
    vk.messages.send(peer_id = chat_id, random_id = random.randint(0, 2**32), message= message)

def create_vk_session(token: str) -> VkApi:
    vk_session = VkApi(token=token)
    return vk_session

def create_message(lesson_link: str, lesson_name: str):
    return f"{lesson_name} \nСсылка на пару: {lesson_link}"


if __name__ == '__main__':
    vk_session = VkApi(token='37b46783ab64430928f8910ebe2f2704675c15c380d0629f80ed4ea932a43dbeeb2a7affb979f19300714')

    longpoll = VkBotLongPoll(vk_session, '189107850')

    for event in longpoll.listen():
        print(event.obj.get('message').get('peer_id'))
        print(send_message_in_chat(chat_id=event.obj.get('message').get('peer_id'), message='Success', vk_session=vk_session))
