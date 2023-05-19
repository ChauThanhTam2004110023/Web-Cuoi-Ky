from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'descriptions', 'quantity', 'images']


class CategoryInventoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'images']


class Register_User(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(Register_User, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter username....'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter email....'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter password1....'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter password2....'})

