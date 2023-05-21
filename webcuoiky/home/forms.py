from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms


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

class RegisterCustomerForm(ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ['name', 'address', 'mobile', 'email']

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = User.objects.create_user(username=username, password=password)

            name = cleaned_data.get('name')
            address = cleaned_data.get('address')
            mobile = cleaned_data.get('mobile')
            email = cleaned_data.get('email')

            customer = Customer(user=user, name=name, address=address, mobile=mobile, email=email)
            customer.save()
            
        return cleaned_data