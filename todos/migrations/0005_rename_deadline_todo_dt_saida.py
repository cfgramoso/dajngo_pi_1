# Generated by Django 5.0.3 on 2024-04-07 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0004_alter_todo_deadline_alter_todo_dt_inicio_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="deadline",
            new_name="dt_saida",
        ),
    ]
