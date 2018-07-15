from django.db import models

GENDER= (
            ('Чоловічий','ЧОЛОВІЧА'),
            ('Жіночий','ЖІНОЧА'),
            ('Інше','Інша')
            )
FAMILY_STATUS = (
            ('Одружений(-а)','MARRIED'),
            ('Неодружений/Незаміжня','SINGLE'),
            ('Вдовець/Вдова','WIDOW'),
            ('Розлучений(-а)','DIVORCED')
            )
AGE= (
            ('18-24','18-24'),
            ('25-29','25-29'),
            ('30-34','30-34'),
            ('35-39','35-39'),
            ('40-54','40-44'),
            ('55-59','55-59'),
            ('60-69','60-69'),
            ('70+','70+')
            )
EDUCATION = (
            ('Вища (магістр / спеціаліст)','master'),
            ('Вища (бакалавр)','bachelor'),
            ('Середня професійна освіта','high school'),
            ('Початкова професійна освіта','unfinished tehcnical education'),
            ('Середня (повна) загальна освіта','finished middle education'),
            ('Початкова загальна освіта','unfinished middle education'),
            )
EXPENDITURES = (
            ('2,500 грн. або меньше','2500'),
            ('3,000 - 4,500 грн.','3000-4500'),
            ('5,000 - 7,000 грн.','5000-7000'),
            ('7,500 - 10,000 грн.','7500-10000'),
            ('12,000 - 15,000 грн.','12000-15000'),
            ('17,000+ грн','17000+')
            )
OCCUPATION = (
            ('Власник(-ця) бізнесу, юридична особа','businessman'),
            ('Фізична особа підприємець','entrepreneur'),
            ('Найманий працівник(-ця)','employed worker'),
            ('Домогосподар(-ка)','housewife'),
            ('Студент(-ка)','student'),
            ('Пенсіонер(-ка)','retired'),
            ('имчасово безробітній(-ня)','unemployed')
            )



class Region(models.Model):
    region_name = models.CharField(max_length=100)
    def __str__(self):
        return self.region_name

class City(models.Model):
    city_name = models.CharField(max_length=100)
    region  = models.ForeignKey(Region,on_delete=models.CASCADE)
    def __str__(self):
        return self.city_name +" "+ self.region.__str__()

# basic class for description of Person's principal info 

class Person(models.Model):
    def __str__(self):
        return self.gender+self.family_status+self.age


    city = models.ForeignKey(City,default=1,on_delete=models.CASCADE)
    gender = models.CharField(max_length=100,default='чоловіча',choices=GENDER)
    family_status=models.CharField(max_length=100,default='married',choices=FAMILY_STATUS)
    age = models.CharField(max_length=100,default='1',choices=AGE)
    education = models.CharField(max_length=100,default='1',choices=EDUCATION)
    expenditures = models.CharField(max_length=100,default='1',choices=EXPENDITURES)
    occupation = models.CharField(max_length=100,default='1',choices=OCCUPATION)
    
    
class Question(models.Model):
    question_text = models.TextField()
    second_question_text = models.TextField(default="Second question",blank=True,null=True)

    def __str__(self):
        return self.question_text
    def get_first_question(self):
        return self.question_text


    def get_second_question(self):
        return self.second_question_text


    

class Answer(models.Model):
    liberal_conservative = models.FloatField()
    conservative_national = models.FloatField()
    national_liberal = models.FloatField()

    def __str__(self):
        return "LC:"+liberal_conservative+":CN:"+conservative_national+":NL:"+national_liberal

    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    person = models.ForeignKey(Person, on_delete= models.CASCADE)







# Create your models here.
