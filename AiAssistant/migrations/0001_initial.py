# Generated by Django 4.2 on 2025-01-08 10:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_message', models.CharField(max_length=1000)),
                ('chat_message', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='StudentContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('studentid', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='Not Mentioned', max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(8)])),
                ('mobile', models.IntegerField()),
                ('college', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='images/')),
                ('percentage', models.SmallIntegerField()),
            ],
        ),
    ]
