from django.contrib import admin
from django import forms
from .models import TestModel
# Register your models here.

class TestModelAdmin(admin.ModelAdmin):
    # Define fields to be displayed in the admin interface
    list_display = ['id', 'name', 'user', 'customer', 'date', 'amount', 'Status', 'type']
    
    # Override formfield_for_foreignkey method to set the user field to the currently logged-in user
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            # Set the user field to the currently logged-in user
            kwargs["initial"] = request.user.id
            # Set the user field to read-only
            kwargs["disabled"] = True
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    # Override save_model method to set the user and logged-in user
    def save_model(self, request, obj, form, change):
        # Set the user field to the currently logged-in user
        obj.user = request.user
        # Call the original save_model method to save the object
        super().save_model(request, obj, form, change)

# Register the TestModelAdmin class with the admin site
admin.site.register(TestModel, TestModelAdmin)
