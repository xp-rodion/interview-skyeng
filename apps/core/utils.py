import ast
from django.conf import settings


def check_code(file: str) -> str:
    with open(f"{settings.MEDIA_ROOT}/{file}") as py_file:
        code = py_file.read()
        try:
            ast.parse(code)
            desc = "Код корректен и готов к исполнению"
        except SyntaxError as e:
            desc = f"Код некорректен. Error - {e}"

        return desc
