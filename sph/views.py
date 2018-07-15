from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import generic
from  .models import Person, Question,Answer,City
from  .forms import PersonForm 
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator




def index(request):
    return render(request,'sph/home.html')


def saver(request):
    if request.method=='POST':
            
            p_gender=request.POST.get('gender')
            p_family_status= request.POST.get('family')
            p_age = request.POST.get('age')
            p_education = request.POST.get('education')
            p_expenditures=request.POST.get('money')
            p_occupation=request.POST.get('job')
            p_city=City.objects.get(id=10)
            person = Person(city=p_city, gender=p_gender,family_status=p_family_status,age=p_age,education=p_education,expenditures=p_expenditures,occupation=p_occupation)
            p_storage = request.POST.getlist('questions')
            print(p_storage)
            print("Hello")
            for p in p_storage:
                print(p)
            
            
            
            person.save()
    else:
            person = PersonForm()
    return render(request,'sph/person_edit.html',{'person':person})
    


def slider(request):
    questions_list =Question.objects.all()
    paginator = Paginator(questions_list,1)
    page = request.GET.get('page')
    questions = paginator.get_page(page)
    return render(request,'sph/questions_paginations.html',{'questions':questions})

    
# returns list of all questions for poll

class QuestionView(generic.ListView):

   
    model = Question
    template_name = 'sph/questions.html'
    context_object_name = 'question_list'

    def get_queryset(self):
       
        return Question.objects.all()

 
    

class PersonView(generic.DetailView):
    model = Person
    template_name = 'sph/person_edit.html'
    def person_new(request):
        if request.method=='POST':
            
            p_gender=request.POST.get('gender')
            p_family_status= request.POST.get('family')
            p_age = request.POST.get('age')
            p_education = request.POST.get('education')
            p_expenditures=request.POST.get('money')
            p_occupation=request.POST.get('job')
            p_city=City.objects.get(id=10)
            person = Person(city=p_city, gender=p_gender,family_status=p_family_status,age=p_age,education=p_education,expenditures=p_expenditures,occupation=p_occupation)
            p_storage = request.POST.getlist('questions')
            print(request.body)
            print(p_storage)
            
            
            
            
            person.save()
        else:
            person = PersonForm()
        return render(request,'sph/person_edit.html',{'person':person})
    


# Create your views here.
