from django import forms
from .models import Question
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Patient

class PatientCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = Patient
        fields = ('username','age','school','grade')
    

class PatientChangeForm(UserChangeForm):

    class Meta:
        model = Patient
        fields = UserChangeForm.Meta.fields

class Question_classCreateForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = [
            'correct_answer'
        ]
