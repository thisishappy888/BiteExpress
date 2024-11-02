from django.contrib import admin
from main.models import Categories
from main.models import Category
from main.models import Burgers

# Register your models here.
admin.site.register(Categories)
admin.site.register(Category)
admin.site.register(Burgers)