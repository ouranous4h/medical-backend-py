# Generated by Django 3.1.7 on 2021-03-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyAPI', '0005_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_doctor',
            name='info',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient_doctor',
            name='time',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
