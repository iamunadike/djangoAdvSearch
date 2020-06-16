from django import forms
from .models import Journal

class JournalForm(forms.ModelForm):
    """form from model fields """
    class Meta:
    	model = Journal
        fields = ('',)
