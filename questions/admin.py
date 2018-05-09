from django.contrib import admin
from .models import Question
from .models import Exam
from .models import Result
from .models import Detailed_Score
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import PatientCreationForm, PatientChangeForm
from .models import Patient



admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Result)
admin.site.register(Detailed_Score)


class CustomUserAdmin(UserAdmin):
    add_form = PatientCreationForm
    form = PatientChangeForm
    model = Patient
    list_display = [
            'patient_ID',
            'username',
            'email', 
            'age',
            'school',
            'grade',
            
            

        ]


admin.site.register(Patient, CustomUserAdmin)


