# Generated by Django 4.1.7 on 2023-03-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
