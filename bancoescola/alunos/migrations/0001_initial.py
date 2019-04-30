# Generated by Django 2.1.7 on 2019-04-30 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alunos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomealunos', models.CharField(max_length=50, verbose_name='Nome')),
                ('siglaalunos', models.CharField(max_length=5, verbose_name='Sigla')),
                ('etiquetaalunos', models.SlugField(verbose_name='Etiqueta')),
            ],
        ),
    ]
