# Generated by Django 4.2.7 on 2024-02-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0006_alter_question_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
