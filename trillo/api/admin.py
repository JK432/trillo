from django.apps import apps
from django.contrib import admin
from .models import *

models = apps.get_models()

admin.site.site_header = 'Admin'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Admin'

admin.site.register(User)
