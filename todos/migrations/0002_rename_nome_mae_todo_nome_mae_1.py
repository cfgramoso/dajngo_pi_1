# Generated by Django 5.0.3 on 2024-04-07 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="nome_mae",
            new_name="nome_mae_1",
        ),
    ]
