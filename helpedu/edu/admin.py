from django.contrib import admin

# Register your models here.
from . models import School,Document
admin.site.register(School)
admin.site.register(Document)