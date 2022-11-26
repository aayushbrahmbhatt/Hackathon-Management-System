from django import forms
from HackathonManagementApp.models import User,Hackathon,Participant

class UserForms(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"

class HackathonForms(forms.ModelForm):
    class Meta:
        model=Hackathon
        fields="__all__"

class ParticipantForms(forms.ModelForm):
    class Meta:
        model=Participant
        fields="__all__"
