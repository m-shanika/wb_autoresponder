from django.core.management.base import BaseCommand
from autoresponder.services import fetch_questions_from_wb

class Command(BaseCommand):
    help = "Парсит все неотвеченные вопросы с WB и сохраняет их в базу данных."

    def add_arguments(self, parser):
        parser.add_argument('--take', type=int, default=100, help='Количество вопросов для получения')
        parser.add_argument('--skip', type=int, default=0, help='Смещение для получения вопросов')

    def handle(self, *args, **options):
        take = options['take']
        skip = options['skip']

        new_questions = fetch_questions_from_wb(take=take, skip=skip)
        self.stdout.write(self.style.SUCCESS(f"Получено {len(new_questions)} новых вопросов с WB."))
