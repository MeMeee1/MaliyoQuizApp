# Generated by Django 3.2.16 on 2023-01-22 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_question_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='correct_option',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='correct_option', to='quiz.questionoption'),
        ),
    ]