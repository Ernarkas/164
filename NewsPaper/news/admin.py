from django.contrib import admin
from .models import Post, Author


class ProductAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = [field.name for field in Post._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения

admin.site.register(Post)
admin.site.register(Author)

# Register your models here.
