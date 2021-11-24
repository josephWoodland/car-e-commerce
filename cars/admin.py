from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):


    def thumbnail(self, object):
        return format_html('<img src="{}" width="60px" style="border-radius: 60px"/>'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Image'

    list_display = ('id', 'car_title', 'thumbnail', 'city', 'color', 'year', 'body_style', 'fuel_type', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')

admin.site.register(Car, CarAdmin)