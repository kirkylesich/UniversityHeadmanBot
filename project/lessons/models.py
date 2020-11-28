from django.db import models

# Create your models here.

class Chat(models.Model):
    chat_id = models.IntegerField()

class LessonLink(models.Model):
    link = models.CharField(max_length=250)

class Lesson(models.Model):
    name = models.CharField(max_length=250)
    link = models.ForeignKey(LessonLink, on_delete=models.CASCADE)
    time = models.DateTimeField()
    lesson_chat = models.ForeignKey(Chat, on_delete=models.CASCADE)


    
