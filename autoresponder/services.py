import time
import requests
from django.utils import timezone
from datetime import datetime
from .models import Question, AnswerTemplate
from .models import Organization
from .gpt_service import get_category_id_for_question


def get_org_token():

    org = Organization.objects.first()
    if org:
        return org.official_token
    return None


def parse_wb_datetime(dt_str):

    dt_str = dt_str.replace('Z', '+00:00')
    if '.' in dt_str:
        main_part, tz_part = dt_str.split('+', 1)
        date_part, time_part = main_part.split('T')

        if '.' in time_part:
            sec_part, micro_part = time_part.split('.', 1)
            micro_part = micro_part[:6]
            main_part = f"{date_part}T{sec_part}.{micro_part}"
        else:
            main_part = f"{date_part}T{time_part}"

        dt_str = f"{main_part}+{tz_part}"

    return datetime.fromisoformat(dt_str)


def fetch_questions_from_wb(take=100, skip=0):

    token = get_org_token()
    if not token:
        return []

    params = {
        'isAnswered': 'false',
        'take': str(take),
        'skip': str(skip),
    }

    url = 'https://feedbacks-api.wildberries.ru/api/v1/questions'
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, params=params, headers=headers)
    data = response.json()
    questions_data = data.get('data', {}).get('questions', [])

    new_questions = []
    for q in questions_data:
        q_id = q.get('id')
        q_text = q.get('text')
        q_created = q.get('createdDate')
        if not q_id or not q_text or not q_created:
            continue

        q_created_dt = parse_wb_datetime(q_created)

        if not Question.objects.filter(question_id=q_id).exists():
            question_obj = Question.objects.create(
                question_id=q_id,
                text=q_text,
                created_date=q_created_dt
            )
            new_questions.append(question_obj)

    return new_questions


def send_answer_to_wb(question, answer_text):

    token = get_org_token()
    if not token:
        return False

    url = 'https://feedbacks-api.wildberries.ru/api/v1/questions'
    payload = {
        "id": question.question_id,
        "answer": {
            "text": answer_text
        },
        "state": "wbRu"
    }

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.patch(url, json=payload, headers=headers)
    result = response.json()
    if not result.get('error', True):
        question.answer_text = answer_text
        question.answer_date = timezone.now()
        question.save()
        return True
    return False


def process_unanswered_questions():

    unanswered = Question.objects.filter(answer_date__isnull=True)
    for q in unanswered:
        category_id = get_category_id_for_question(q.text)
        if category_id:
            try:
                template = AnswerTemplate.objects.get(category_id=category_id)
            except AnswerTemplate.DoesNotExist:
                continue
            answer_text = template.answer_text
            send_answer_to_wb(q, answer_text)
