from django.contrib import admin
from lessons.models import Lesson, LessonLink, Chat

# Register your models here.

class LessonLinkAdmin(admin.ModelAdmin):
    pass

class LessonAdmin(admin.ModelAdmin):
    pass

class ChatAdmin(admin.ModelAdmin):
    pass


admin.site.register(LessonLink, LessonLinkAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Chat, ChatAdmin)
