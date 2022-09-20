from django.contrib import admin
from product.models import Users,Product

models = [Users,Product]

admin.site.register(models)