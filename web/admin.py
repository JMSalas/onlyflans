from django.contrib import admin
from .models import Flan, ContactForm, Review

# Register your models here.
@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('flan_uuid', 'name','description','precio', 'image_url','slug','is_private')
    search_fields = ('name',)
    list_filter = ('is_private',)
    
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('contact_form_uuid', 'customer_email','customer_name','message')
    search_fields = ('customer_email','customer_name')
