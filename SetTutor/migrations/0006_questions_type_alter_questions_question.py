# Generated by Django 4.1.7 on 2023-03-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SetTutor', '0005_alter_questions_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='Type',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='questions',
            name='Question',
            field=models.CharField(max_length=512),
        ),
    ]
