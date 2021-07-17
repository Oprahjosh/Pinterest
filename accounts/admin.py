from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser
# Register your models here.
class CustomAdmin(UserAdmin):
    list_display = ('email','Age','is_staff')
    search_fields = ('email','Age')
    readonly_fields = ('id','date_joined')

    filter_horizontal = ()
    list_filter = ()
    Fieldsets = ()

    ordering = ('email' ,)


admin.site.register(CustomUser,CustomAdmin)