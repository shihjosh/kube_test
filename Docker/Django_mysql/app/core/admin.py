from django.contrib import admin

# Register your models here.
from core.models import Sample
from core.models import Music

admin.site.register(Sample)
admin.site.register(Music)
