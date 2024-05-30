from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Country, State, City

# Register your models here.

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)

class AccountAdmin(UserAdmin):
    list_display = ('username', 'last_name', 'email', 'last_login', 'date_joined', 'is_staff', 'is_active', 'is_superuser')
    search_fields = ('username', 'first_name', 'last_name')
    readonly_fields = ('id',)
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(User, AccountAdmin)