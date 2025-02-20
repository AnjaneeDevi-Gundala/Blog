from django.contrib import admin
from .models import createModel
# Register your models here.
class retrieveAdmin(admin.ModelAdmin):
    list_display=['img','title','description','author']
admin.site.register(createModel,retrieveAdmin)