from django.contrib import admin
from .models import UserInfo,Plant,PlantDisease
# Register your models here.
admin.site.register(PlantDisease)
admin.site.register(UserInfo)
admin.site.register(Plant)