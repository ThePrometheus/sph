# Generated by Django 2.0.7 on 2018-07-15 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sph', '0006_auto_20180715_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.CharField(choices=[('18-24', '18-24'), ('25-29', '25-29'), ('30-34', '30-34'), ('35-39', '35-39'), ('40-54', '40-44'), ('55-59', '55-59'), ('60-69', '60-69'), ('70+', '70+')], default='25-29', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='education',
            field=models.CharField(choices=[('Вища (магістр / спеціаліст)', 'master'), ('Вища (бакалавр)', 'bachelor'), ('Середня професійна освіта', 'high school'), ('Початкова професійна освіта', 'unfinished tehcnical education'), ('Середня (повна) загальна освіта', 'finished middle education'), ('Початкова загальна освіта', 'unfinished middle education')], default='Початкова загальна освіта', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='expenditures',
            field=models.CharField(choices=[('2,500 грн. або меньше', '2500'), ('3,000 - 4,500 грн.', '3000-4500'), ('5,000 - 7,000 грн.', '5000-7000'), ('7,500 - 10,000 грн.', '7500-10000'), ('12,000 - 15,000 грн.', '12000-15000'), ('17,000+ грн', '17000+')], default='3,000 - 4,500 грн.', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='occupation',
            field=models.CharField(choices=[('Власник(-ця) бізнесу, юридична особа', 'businessman'), ('Фізична особа підприємець', 'entrepreneur'), ('Найманий працівник(-ця)', 'employed worker'), ('Домогосподар(-ка)', 'housewife'), ('Студент(-ка)', 'student'), ('Пенсіонер(-ка)', 'retired'), ('имчасово безробітній(-ня)', 'unemployed')], default='Власник(-ця) бізнесу, юридична особа', max_length=100),
        ),
    ]
