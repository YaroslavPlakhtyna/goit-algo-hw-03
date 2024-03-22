""" Завдання 1:
 Напишіть програму на Python, яка рекурсивно копіює файли у вихідній директорії, переміщає їх до нової директорії та сортує в піддиректорії, 
 назви яких базуються на розширенні файлів.
 
 Також візьміть до уваги наступні умови:
 
 1. Парсинг аргументів. Скрипт має приймати два аргументи командного рядка: шлях до вихідної директорії та шлях до директорії призначення
 (за замовчуванням, якщо тека призначення не була передана, вона повинна бути з назвою dist).
 2. Рекурсивне читання директорій:
   Має бути написана функція, яка приймає шлях до директорії як аргумент.
   Функція має перебирати всі елементи у директорії.
   Якщо елемент є директорією, функція повинна викликати саму себе рекурсивно для цієї директорії.
   Якщо елемент є файлом, він має бути доступним для копіювання.
 3. Копіювання файлів:
   Для кожного типу файлів має бути створений новий шлях у вихідній директорії, використовуючи розширення файлу для назви піддиректорії.
   Файл з відповідним типом має бути скопійований у відповідну піддиректорію.
 4. Обробка винятків. Код має правильно обробляти винятки, наприклад, помилки доступу до файлів або директорій.
"""

import shutil

from argparse import ArgumentParser
from pathlib import Path


def copy_tree(source: Path, dest: str) -> None:
    source = Path(source)
    if not source.exists():
        raise ValueError("Source path must be valid.")
    print(source.name)
    if source.is_dir():
        for child in source.iterdir():
            copy_tree(child, dest)
    elif source.is_file():
        dest_dir = Path(dest) / source.suffix
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(source, dest_dir / source.name)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-s", "--source", help="path to the source dir")
    parser.add_argument(
        "-d",
        "--dest",
        default="dist",
        help="path to the destination dir (defaults to 'dist')",
    )
    args = parser.parse_args()
    copy_tree(args.source, args.dest)