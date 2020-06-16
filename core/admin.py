from django.contrib import admin
from .models import Author, Journal, Category
# Register your models here.

admin.site.register(Author,)
admin.site.register(Journal)
admin.site.register(Category)