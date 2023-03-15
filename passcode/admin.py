from django.contrib import admin
from .models import Question, Notice, images

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QuestionAdmin)

class NoticeAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Notice, NoticeAdmin)

class ImagesAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(images, ImagesAdmin)