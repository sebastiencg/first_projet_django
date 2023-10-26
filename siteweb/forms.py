from django import forms
from django.forms import ModelForm

# import GeeksModel from models.py
from .models import Message, Category, Response
from .models import User


# create a ModelForm
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'category']

    category = forms.ModelChoiceField(queryset=Category.objects.all())


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['content']


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
