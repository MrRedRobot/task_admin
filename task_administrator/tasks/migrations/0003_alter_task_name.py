# Generated by Django 4.1.4 on 2022-12-07 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_delete_comentary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
