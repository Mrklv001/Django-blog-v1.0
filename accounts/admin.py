from django.contrib import admin
from accounts.models import Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Profile)
class MyProfile(SummernoteModelAdmin):
    summernote_fields = ('bio',)
