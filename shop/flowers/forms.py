from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Catalog, Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']
        labels = {
            'quantity': ('Количество'),
        }


class ProductForm(ModelForm):
    class Meta:
        model = Catalog
        fields = ['product', 'category', 'price', 'quantity', 'foto']
        labels = {
            'product': ('Товар'),
            'category': ('Категория'),
            'price': ('Цена'),
            'quantity': ('Количество'),
            'foto': ('Картинка'),
        }

    def clean(self):
        cleaned_data = super(ProductForm, self).clean()
        usrs = Catalog.objects.filter(product=cleaned_data.get('product'))
        if len(usrs) > 0:
            raise forms.ValidationError("Данный товар уже существует")


class LoginForm(forms.Form):
    login = forms.CharField(label='Логин', min_length=5)
    password = forms.CharField(label='Пароль', min_length=8, widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    login = forms.CharField(label='Логин', min_length=5)
    password = forms.CharField(label='Пароль', min_length=8, widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', min_length=8, widget=forms.PasswordInput)
    email = forms.CharField(label='Email', min_length=1)
    firstname = forms.CharField(label='Имя', min_length=1)
    lastname = forms.CharField(label='Фамлия', min_length=1)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Пароли не совпадают")
        usrs = User.objects.filter(username=cleaned_data.get('login'))
        if len(usrs) > 0:
            raise forms.ValidationError("Пользователь с данным логином уже существует")