# Generated by Django 4.2.2 on 2023-06-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Введите имя')),
                ('number', models.CharField(max_length=250, verbose_name='Введите номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.CharField(max_length=250, verbose_name='Введите текст')),
            ],
        ),
    ]