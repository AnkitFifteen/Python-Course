from django.contrib import admin
from .models import Pet

# Register your models here.
class PetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name','species','breed')}

admin.site.register(Pet,PetAdmin)