# Generated by Django 4.1.7 on 2023-03-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SetTutor', '0004_remove_questions_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='Question',
            field=models.CharField(max_length=512, unique=True),
        ),
    ]
