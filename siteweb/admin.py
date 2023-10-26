from django.contrib import admin

# Register your models here.

from .models import Message, User, Category, Response

admin.site.register(Message)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Response)