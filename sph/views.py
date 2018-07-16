from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import generic
from  .models import Person, Question,Answer,City,BLOCKS,TYPES
from  .forms import PersonForm 
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
import json 




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
    @csrf_exempt
    def person_new(request):
        if request.method=='POST':
            data=json.loads(request.body)
            
            p_gender=data['gender']
            p_family_status= data['family']
            print(p_family_status)
            p_age = data['age']
            
            p_education = data['education']
            p_expenditures= data['expenditures']
            p_occupation= data['occupation']
            p_city=City.objects.get(id=10)
            person = Person(city=p_city, gender=p_gender,family_status=p_family_status,age=p_age,education=p_education,expenditures=p_expenditures,occupation=p_occupation)
            p_storage = data['questions']
            
            person.save()
            print(p_storage)
            
            
            for b_key,b_value in BLOCKS:
                for i in range(1,8):
                    answer=Answer.objects.create(person=person)
                    answer.save()
                    
                    
                    lc=0
                    cs=0
                    sn=0
                    ln=0
                    ls=0
                    cn=0
                    question_set=Question.objects.filter(tag_id=i,block=b_key)
                    for obj in question_set:
                        if obj.type_block=='LC':
                            lc=float(p_storage[str(obj.id)])
                            print("LC:"+str(lc))
                            answer.questions.add(obj)
                   
                   
                        elif obj.type_block=='CS':
                            cs=float(p_storage[str(obj.id)])
                            print("CS:"+str(cs))
                            answer.questions.add(obj)
                    
                    
                        else:
                            sn=float(p_storage[str(obj.id)])
                            print("SN:"+str(sn))
                            answer.questions.add(obj)
                    ls=abs(lc)+abs(cs)
                    cn=abs(cs)+abs(sn)
                    ln=abs(ls)+abs(cn)-abs(cs)
                    answer.liberal_conservative=lc
                    answer.conservative_social=cs               
                    answer.liberal_social=ls
                    answer.liberal_national=ln
                    answer.social_national=sn
                    answer.conservative_national=cn
                    print(answer.questions.all())
                    answer.save()
                    
                    
                    
                    
                        
                    
           
            
            
            
            
            
            
        else:
            person = PersonForm()
        return render(request,'sph/person_edit.html',{'person':person})
    


# Create your views here.
