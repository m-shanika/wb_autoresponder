from celery import shared_task
from .services import process_unanswered_questions

@shared_task
def daily_process_unanswered():
    """
    Ежедневная задача для обработки всех неотвеченных вопросов.
    """
    process_unanswered_questions()
