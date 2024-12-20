from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    'process_unanswered_questions_daily': {
        'task': 'apps.questions.tasks.daily_process_unanswered',
        'schedule': crontab(hour=0, minute=0),  # каждый день в полночь
    },
}
