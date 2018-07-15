from django import forms 
from .models import Person,FAMILY_STATUS,AGE,EDUCATION,EXPENDITURES,OCCUPATION,City

class PersonForm(forms.ModelForm):
    """print(GENDER)
    
    gender = forms.ModelChoiceField(queryset=GENDER)
    family_status = forms.ModelChoiceField(queryset=FAMILY_STATUS)
    age = forms.ModelChoiceField(queryset=AGE)
    education =forms.ModelChoiceField(queryset=EXPENDITURES)
    occupation = forms.ModelChoiceField(queryset=OCCUPATION) 
   
                                 
    """
    class Meta:
        model = Person
        fields = ['city','gender','family_status','age','education','expenditures','occupation']
        


       