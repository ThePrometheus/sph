# Generated by Django 2.0.6 on 2018-07-01 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sph', '0003_auto_20180625_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='second_question_text',
            field=models.TextField(blank=True, default='Second question', null=True),
        ),
    ]
