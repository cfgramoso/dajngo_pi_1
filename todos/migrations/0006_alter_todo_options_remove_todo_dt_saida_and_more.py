# Generated by Django 5.0.4 on 2024-04-08 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0005_rename_deadline_todo_dt_saida"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="todo",
            options={"ordering": ["nome_aluno"]},
        ),
        migrations.RemoveField(
            model_name="todo",
            name="dt_saida",
        ),
        migrations.AlterField(
            model_name="todo",
            name="cpf_mae",
            field=models.CharField(max_length=100, verbose_name="CPF da Mãe"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="cpf_pai",
            field=models.CharField(max_length=100, verbose_name="CPF do Pai"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="endereco",
            field=models.CharField(max_length=100, verbose_name="Endereço"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="mensalidade",
            field=models.CharField(max_length=100, verbose_name="Mensalidade"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="nome_aluno",
            field=models.CharField(max_length=100, verbose_name="Nome do Aluno"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="nome_mae",
            field=models.CharField(max_length=100, verbose_name="Nome da Mãe"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="nome_pai",
            field=models.CharField(max_length=100, verbose_name="Nome do Pai"),
        ),
        migrations.AlterField(
            model_name="todo",
            name="telefone",
            field=models.CharField(max_length=100, verbose_name="Telefone"),
        ),
    ]
