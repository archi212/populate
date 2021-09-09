from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Webpage)
admin.site.register(Access_Records)
admin.site.register(Topic)
 
