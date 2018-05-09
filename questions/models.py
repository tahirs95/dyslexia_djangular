from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

User = settings.AUTH_USER_MODEL

class Patient(AbstractUser):
    
   
    patient_ID = models.AutoField(primary_key=True)
    # email = models.EmailField(default = '', verbose_name='email address', max_length=255, unique=True, null=True)
    age = models.IntegerField(null=True)
    school = models.CharField(max_length=50, default='')
    grade = models.IntegerField(null=True)
    gender = models.CharField(max_length=50, default='')

    USERNAME_FIELD = 'username'


    def __str__(self):
        return str(self.patient_ID)



class Question(models.Model):
    #owner = models.ForeignKey(User, on_delete=models.CASCADE) #class_instance.model_set.all()
    ques_ID = models.AutoField(primary_key=True)
    audio = models.FileField(null=True, blank=True, upload_to="audios/")
    correct_answer = models.CharField(max_length=50, default='')


class Exam(models.Model):
    exam_ID = models.AutoField(primary_key=True)
    patient_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.exam_ID)
	
	

class Result(models.Model):
    res_ID = models.AutoField(primary_key=True)
    exam_ID = models.ForeignKey(Exam, on_delete=models.CASCADE)
    p_ID = models.ForeignKey(Patient, on_delete=models.CASCADE, default='')
    hits = models.IntegerField()
    misses = models.IntegerField()
    accuracy = models.FloatField()
		
class Detailed_Score(models.Model):
    exam_ID = models.ForeignKey(Exam, on_delete=models.CASCADE)
    ques_ID = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_submitted = models.CharField(max_length=50, default='')
    class Meta:
        unique_together = (('exam_ID', 'ques_ID'),)
	


			
   