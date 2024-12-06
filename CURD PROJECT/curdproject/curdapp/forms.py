from django import forms
from .models import Enquiry

class Enquiry_forms(forms.ModelForm):
    class Meta:
        model = Enquiry

        fields = [
            'name',
            'email',
            'contact',
            'course'
        ]