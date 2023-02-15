from django.contrib import admin
from iphoneapp.models import iphone14

# Register your models here.
class iphone14Admin(admin.ModelAdmin):
    list_display=['name','version','maincamera','rearcamera','battery','display','memory',]
admin.site.register(iphone14,iphone14Admin);

