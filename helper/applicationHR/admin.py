from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Summary, Positions, Personnel,Employees, Cards
class UserAdmin(UserAdmin):
    list_display = ('username', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('username', 'phone',)
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)
admin.site.register(Summary)
admin.site.register(Positions)
admin.site.register(Personnel)
admin.site.register(Employees)
admin.site.register(Cards)