# Generated by Django 3.1.7 on 2021-03-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyAPI', '0006_auto_20210314_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_doctor',
            name='info',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='patient_doctor',
            name='time',
            field=models.CharField(max_length=30),
        ),
    ]