# Generated by Django 4.1.7 on 2023-03-13 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SetTutor', '0003_questions_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='Size',
        ),
    ]