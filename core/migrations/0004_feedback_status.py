# Generated by Django 3.0.1 on 2020-01-16 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_feedback_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]