import openai
from .models import AnswerTemplate
from backend.settings import OPENAPI_KEY

openai.api_key = OPENAPI_KEY

def get_category_id_for_question(question_text):

    categories = AnswerTemplate.objects.all()
    if not categories.exists():
        return None

    category_list_str = "\n".join([f"Категория: {c.category_name}, ID: {c.category_id}" for c in categories])
    prompt = (
       f"Ниже приведён вопрос:\n"
       f"'{question_text}'\n\n"
       f"Есть следующие категории вопросов:\n"
       f"{category_list_str}\n\n"
       f"Проанализируй вопрос, пройдись по каждой категории и выбери наиболее подходящую. "
       f"Если вопрос не относится ни к одной категории, то верни ответ 0.\n"
       f"Верни только ID категории, без лишних слов, без кавычек."
    )

    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{'role': 'user', 'content': prompt}],
        temperature=0.0,
    )

    category_id = response.choices[0].message.content.strip()
    return category_id
