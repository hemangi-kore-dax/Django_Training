# Generated by Django 3.2.14 on 2022-07-19 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_todo_done_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]