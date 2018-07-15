from django.urls import path 

from . import views 

urlpatterns = [
        path('home', views.index, name='index'),
        path('slider', views.slider, name='slider'),
        path('questions',views.QuestionView.as_view(), name='questions_list'),
    path('person/new/', views.PersonView.person_new, name='person_new'),
    
        ]
