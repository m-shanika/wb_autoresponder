# Generated by Django 5.1.4 on 2024-12-12 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(max_length=255, unique=True, verbose_name='ID категории')),
                ('category_name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('answer_text', models.TextField(verbose_name='Шаблонный ответ')),
            ],
            options={
                'verbose_name': 'Шаблон ответа',
                'verbose_name_plural': 'Шаблоны ответов',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название организации')),
                ('token', models.CharField(max_length=255, verbose_name='Токен для API')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.CharField(max_length=255, unique=True, verbose_name='ID вопроса')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('created_date', models.DateTimeField(verbose_name='Дата создания вопроса')),
                ('answer_text', models.TextField(blank=True, null=True, verbose_name='Текст ответа')),
                ('answer_date', models.DateTimeField(blank=True, null=True, verbose_name='Дата ответа')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]