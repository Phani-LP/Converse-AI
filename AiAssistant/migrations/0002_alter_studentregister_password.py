# Generated by Django 4.2 on 2025-01-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AiAssistant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentregister',
            name='password',
            field=models.CharField(max_length=32),
        ),
    ]
