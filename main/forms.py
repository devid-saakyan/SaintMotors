from django import forms
from .models import CarSubmission

class CarSubmissionForm(forms.ModelForm):
    class Meta:
        model = CarSubmission
        fields = '__all__'


class CallBackForm(forms.ModelForm):
    class Meta:
        model = CarSubmission
        fields = '__all__'