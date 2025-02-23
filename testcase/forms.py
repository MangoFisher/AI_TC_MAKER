from django import forms
from .models import TestCase

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['name', 'description', 'steps', 'expected_result', 'status'] 