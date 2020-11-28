from datetime import datetime, timedelta
from celery import shared_task
from celery.schedules import crontab

from bot.lib import send_message_in_chat, create_vk_session, create_message
from project.settings import GROUP_TOKEN
from vk_api import VkApi
from project.celery import app
from lessons.models import Chat

@shared_task
def send_message(chat_id: int, message: str):
    vk_session = VkApi(token=GROUP_TOKEN)
    send_message_in_chat(chat_id, message, vk_session)

@shared_task
def register_lesson_send(chat_id: int, message:str, datetime: datetime):
    print("kek!")
    send_message.apply_async((chat_id, message), eta=datetime)



@shared_task
def send_all_chats():
    chats = Chat.objects.all()
    for chat in chats:
        for lesson in chat.lesson_set.all():
            register_lesson_send.delay(chat.chat_id, create_message(lesson.link, lesson.name), datetime=lesson.time)

