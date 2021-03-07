# Generated by Django 3.1.7 on 2021-03-07 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyAPI', '0003_auto_20210308_0137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(max_length=30)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyAPI.clinic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyAPI.user')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyAPI.user')),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyAPI.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyAPI.patient')),
            ],
        ),
    ]
