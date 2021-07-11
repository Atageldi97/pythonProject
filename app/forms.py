from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *


class CreateReklam(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    spec = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    brand = forms.ModelChoiceField(queryset=Brands.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(queryset=SubCategory.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    city = forms.ModelMultipleChoiceField(queryset=Address.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    price = FloatField()
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    cheep = forms.BooleanField(required=False)

    class Meta:
        model = Reklam
        fields = ('name', 'category', 'brand', 'category', 'address', 'price', 'text', 'cheep',)


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ()
        widgets = {'url': forms.HiddenInput}


