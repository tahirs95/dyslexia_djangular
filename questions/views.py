from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from .models import Question,Patient,Result,Exam
from .forms import Question_classCreateForm
# from patients.models import Patient

from django.urls import reverse_lazy
from django.views import generic

from .forms import PatientCreationForm

class SignUp(generic.CreateView):
    form_class = PatientCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class QListView(ListView):
    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)

# def question_view(request):
#     template_name = 'questions/q_list.html'
# 	#queryset = Patient.objects.filter(p_name__iexact='tahir')
#     queryset = Patient.objects.all()
#     q = Question.objects.all()
#     context = { 'obj_list' : queryset ,'q_list': q}
#     return render(request, template_name, context)

def index(request):
    return HttpResponse('<h1>Hello World, its my first live website.</h1>')
def p_login(request):
   
    template_name = 'plog.html'
    queryset = Patient.objects.all()
    context = { 'names_list' : queryset}
    return render(request, template_name, context)

def result(request):
    template_name = 'result.html'
    queryset = Result.objects.prefetch_related('p_ID','exam_ID').order_by('-hits')
    context = { 'result_list' : queryset}
    return render(request, template_name, context)







class QDetailView(ListView):
    model = Question
    template_name = 'questions/question_list.html'
    context_object_name = 'obj_list' 


class QUpdateView(UpdateView):
    model = Question
    form_class = Question_classCreateForm
    template_name = 'patientsHTML/forms.html'
    success_url = "/question/view/"

class QcreateView ( CreateView ):
	form_class = Question_classCreateForm
	template_name = 'patientsHTML/forms.html'
	#login_url = '/login/'
	success_url = "/question/view/"

	def get_context_data(self, *args, **kwargs):
		context = super(QcreateView, self).get_context_data(*args, **kwargs)
		context['title'] = 'Add Question'
		return context

	
    
    

