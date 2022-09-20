from dataclasses import fields
from django.forms import ModelForm
from product.models import Users,Product


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
            
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        