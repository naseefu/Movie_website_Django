from django.contrib import admin

# Register your models here.

from . models import Category,Movie

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Movie,ProductAdmin)