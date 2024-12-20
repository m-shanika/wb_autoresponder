from django.core.management.base import BaseCommand
from autoresponder.gpt_service import get_category_id_for_question

class Command(BaseCommand):
    help = "Тестирование исключительно логики GPT для определения категории."

    def add_arguments(self, parser):
        parser.add_argument('--question', type=str, help='Текст вопроса для проверки логики GPT')

    def handle(self, *args, **options):
        question_text = options.get('question')

        if not question_text:
            self.stdout.write(self.style.ERROR("Необходимо передать аргумент --question с текстом вопроса"))
            return

        category_id = get_category_id_for_question(question_text)
        if category_id:
            self.stdout.write(self.style.SUCCESS(f"GPT определил категорию с ID: {category_id}"))
        else:
            self.stdout.write(self.style.WARNING("GPT не смог определить категорию для этого вопроса."))
