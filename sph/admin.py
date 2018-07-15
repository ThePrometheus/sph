from django.contrib import admin
from .models import Region, City,Person,Question,Answer 

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text','second_question_text']

admin.site.register(Question, QuestionAdmin)



admin.site.register(City)
admin.site.register(Region)
admin.site.register(Person)
admin.site.register(Answer)

# Register your models here.
