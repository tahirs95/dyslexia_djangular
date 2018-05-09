from django.contrib.auth.models import User, Group
from rest_framework import serializers
from questions.models import Question
# from patients.models import Patient
from questions.models import Result
from questions.models import Exam
from questions.models import Detailed_Score
from questions.models import Patient

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('ques_ID','audio', 'correct_answer')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('patient_ID', 'email','age','school','grade','gender')

class LoginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('patient_ID', 'email','age','school','grade','gender')
    def save(self):
        user =  self.context['request'].user


# class PatientSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
        
#         model = Patient
#         fields = ('patient_ID', 'first_name', 'last_name','age','p_dob','school','grade', 'password', 'p_email')

# class PatientCreateSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
        
#         model = Patient
#         fields = ('first_name', 'last_name','age','p_dob','school','grade', 'password', 'p_email')
#         read_only_fields = ['owner']

class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = ('res_ID', 'p_ID', 'exam_ID', 'hits', 'misses', 'accuracy')

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exam
        fields = ('exam_ID', 'patient_ID')
        
class Detailed_ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Detailed_Score
        fields = ('exam_ID', 'ques_ID', 'answer_submitted')