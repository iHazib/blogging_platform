from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# viewed all the fields of the CustomUser model coming into the admin site.
# u = CustomUser.objects.first()
# print(u)

#Note: the is_staff field is used to determine if the user can log into the admin site or not. And it is separate from the role field. 

@admin.register(CustomUser) # a decorator to register the custom user model with the admin site.
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'name', 'role', 'is_staff') #added name and role to the list display. 
    list_filter = ('role', 'is_staff') # filters used to filter the users based on their roles and staff status. 

    # extra fieldsets added to the default fieldsets of the UserAdmin class.

    fieldsets = UserAdmin.fieldsets + ( 
      ('Extra Info', {'fields': ('name', 'mobile', 'role')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {'fields': ('name', 'mobile', 'role')}),
    )

    




    
