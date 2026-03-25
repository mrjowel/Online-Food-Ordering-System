from django.contrib import admin
from .models import Room,Message

# Register your models here.
admin.site.site_header= "Foodie | Admin"
admin.site.register(Room)
admin.site.register(Message)