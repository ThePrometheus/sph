# Generated by Django 2.0.6 on 2018-06-25 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sph', '0002_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liberal_conservative', models.FloatField()),
                ('conservative_national', models.FloatField()),
                ('national_liberal', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sph.City'),
        ),
        migrations.AddField(
            model_name='answer',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sph.Person'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sph.Question'),
        ),
    ]