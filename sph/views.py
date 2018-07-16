from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import generic
from  .models import Person, Question,Answer,City,BLOCKS,TYPES
from  .forms import PersonForm 
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
import json 
import csv




def index(request):
	return render(request,'sph/home.html')

def results(request):
	
	resultFields=[]
	resultFields.append('person_id')
	for b_key, b_value in BLOCKS:
		if b_key =='Економічний':
			for i in range(1,7):
				resultFields.append(b_key+"_"+str(i)+"_"+"LC")
				resultFields.append(b_key+"_"+str(i)+"_"+"CS")
				resultFields.append(b_key+"_"+str(i)+"_"+"CN")
				resultFields.append(b_key+"_"+str(i)+"_"+"LS")
				resultFields.append(b_key+"_"+str(i)+"_"+"LN")
				resultFields.append(b_key+"_"+str(i)+"_"+"SN")
				
		else :
			for i in range(1,8):
				resultFields.append(b_key+"_"+str(i)+"_"+"LC")
				resultFields.append(b_key+"_"+str(i)+"_"+"CS")
				resultFields.append(b_key+"_"+str(i)+"_"+"CN")
				resultFields.append(b_key+"_"+str(i)+"_"+"LS")
				resultFields.append(b_key+"_"+str(i)+"_"+"LN")
				resultFields.append(b_key+"_"+str(i)+"_"+"SN")
	resultFields.append("gender")
	resultFields.append("city")
	resultFields.append("family_status")
	resultFields.append("age")
	resultFields.append("education")
	resultFields.append("expenditures")
	resultFields.append("occupation")
	
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="results.csv"'
	writer = csv.DictWriter(response,fieldnames = resultFields)
	writer.writeheader()
	persons_list = Person.objects.all()
	for p in persons_list:
		value={'person_id':p.id}
		answers_list = p.answer_set.all()
		for a in answers_list:
			questions_list=a.questions.all()
			for q in questions_list:
				value[str(q.block+"_"+str(q.tag_id)+"_"+"LC")]=a.liberal_conservative
				value[str(q.block+"_"+str(q.tag_id)+"_"+"CS")]=a.conservative_social
				value[str(q.block+"_"+str(q.tag_id)+"_"+"CN")]=a.conservative_national
				value[str(q.block+"_"+str(q.tag_id)+"_"+"LS")]=a.liberal_social
				value[str(q.block+"_"+str(q.tag_id)+"_"+"LN")]=a.liberal_national
				value[str(q.block+"_"+str(q.tag_id)+"_"+"SN")]=a.social_national

		value["gender"]=p.gender
		value["city"]=p.city.__str__()
		value["family_status"]=p.family_status
		value["age"]=p.age
		value["education"]=p.education
		value["expenditures"]=p.expenditures
		value["occupation"]=p.occupation
		writer.writerow(value)	
	return response

			   

					
					
					
				
	
	
	
	


def saver(request):
	
	print(city_set)
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
			
			

			return render(request,'sph/person_edit.html',{'cities':city_set})
	print("FINE")	
	'''person = PersonForm()'''
	return render(request,'sph/person_edit.html',{'cities':city_set})
	


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
		city_set = City.objects.all()
		if request.method=='POST':
			data=json.loads(request.body)
			
			p_gender=data['gender']
			p_family_status= data['family']
			
			p_age = data['age']
			
			p_education = data['education']
			p_expenditures= data['expenditures']
			p_occupation= data['occupation']
			p_city_id = data['city']
			p_city=City.objects.get(id=p_city_id)
			person = Person(city=p_city, gender=p_gender,family_status=p_family_status,age=p_age,education=p_education,expenditures=p_expenditures,occupation=p_occupation)
			p_storage = data['questions']
			
			person.save()
			
			
			
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
							
							answer.questions.add(obj)
				   
				   
						elif obj.type_block=='CS':
							cs=float(p_storage[str(obj.id)])
							
							answer.questions.add(obj)
					
					
						else:
							sn=float(p_storage[str(obj.id)])
							
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
					
					answer.save()
					
					
					
					
						
					
		   
			
			
			
			
			
			
		else:
			return render(request,'sph/person_edit.html',{'cities':city_set})
			'''person = PersonForm()'''
		return render(request,'sph/person_edit.html',{'person':person})
	


# Create your views here.
