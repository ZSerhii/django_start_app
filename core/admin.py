from django.contrib import admin
from core.models import Feedback, Subject, Messanger, Bot

# Register your models here.


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'status', 'created')
    list_editable = ('status',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)


@admin.register(Messanger)
class MessangerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active')
    list_editable = ('is_active',)


@admin.register(Bot)
class BotAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'messanger', 'is_active')
    list_editable = ('is_active',)
