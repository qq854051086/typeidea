from django.contrib import admin

# Register your models here.
from .models import Link, SideBar

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title','href','status','weight','created_time')
    fields = ('title','href','status','weight','created_time')
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(LinkAdmin, self).save_model(request, obj, form, change)

@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('title','display_name','content','status','created_time')
    fields = ('title','display_name','content','created_time')
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SideBarAdmin, self).save_model(request, obj, form, change)
