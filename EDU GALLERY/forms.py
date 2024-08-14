from django import forms
from.models import Multipleimage
class MultipleImageUploadForm(forms.ModelForm):
    class Meta:
        model= Multipleimage
        fields =["image"]
