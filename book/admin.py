from django.contrib import admin

# Register your models here.
from .models import books,author

admin.site.register(books)
admin.site.register(author)