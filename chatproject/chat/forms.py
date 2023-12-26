from django import forms
from .models import Room, Message

class CreateRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('name',)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content',)