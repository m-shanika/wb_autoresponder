from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название организации")
    official_token = models.TextField(max_length=255, verbose_name="Токен для API")

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return self.name

class Question(models.Model):
    question_id = models.CharField(max_length=255, unique=True, verbose_name="ID вопроса")
    text = models.TextField(verbose_name="Текст вопроса")
    created_date = models.DateTimeField(verbose_name="Дата создания вопроса")
    answer_text = models.TextField(null=True, blank=True, verbose_name="Текст ответа")
    answer_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата ответа")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return f"Вопрос {self.question_id}"

class AnswerTemplate(models.Model):
    category_id = models.CharField(max_length=255, unique=True, verbose_name="ID категории")
    category_name = models.CharField(max_length=255, verbose_name="Название категории")
    answer_text = models.TextField(verbose_name="Шаблонный ответ")

    class Meta:
        verbose_name = "Шаблон ответа"
        verbose_name_plural = "Шаблоны ответов"

    def __str__(self):
        return f"Категория: {self.category_name}"
