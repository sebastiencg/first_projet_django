from django import forms

# import GeeksModel from models.py
from .models import Message


# create a ModelForm
class MessageForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Message
        fields = "__all__"