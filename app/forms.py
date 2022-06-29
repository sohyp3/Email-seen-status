from django import  forms
from .models import infoModel

class infoForm(forms.ModelForm):
    class Meta:
        model = infoModel
        fields = ["tracker","notes"]