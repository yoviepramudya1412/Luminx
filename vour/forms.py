from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):

    class Meta:
        model = Candidate
        fields = ("name","phone","email","gender","career")
        labels = {
            'name': 'Name',
            'email':'Email',
        }
        #placeholder
        widget = {
            'name': forms.TimeInput(attrs={'placeholder':'Your name'}),
            'phone': forms.TimeInput(attrs={'placeholder':'Your phone'}),
            'email': forms.TimeInput(attrs={'placeholder':'Your email'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(CandidateForm,self).__init__(*args, **kwargs)
        self.fields['gender'].choices = [("","Select a gender"),] + list(self.fields['gender'].choices)[1:]
        self.fields['career'].empty_tables =  "Select an option"
        self.fields['email'].required = True
        
