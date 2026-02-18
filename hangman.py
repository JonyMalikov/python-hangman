"""
Hangman Game
Простая консольная игра "Виселица"
"""

import random
from typing import LiteralString


# ASCII-арты для виселицы (7 состояний)
HANGMAN_PICS = [
    # 0 ошибок
    """
     _______
    |/      |
    |
    |
    |
    |
    |
    |__""",
    # 1 ошибка
    """
     _______
    |/      |
    |      😊
    |
    |
    |
    |
    |__""",
    # 2 ошибки
    """
     _______
    |/      |
    |      😊
    |       |
    |
    |
    |
    |__""",
    # 3 ошибки
    """
     _______
    |/      |
    |      😊
    |      /|
    |
    |
    |
    |__""",
    # 4 ошибки
    """
     _______
    |/      |
    |      😊
    |      /|\\
    |
    |
    |
    |__""",
    # 5 ошибок
    """
     _______
    |/      |
    |      😊
    |      /|\\
    |      /
    |
    |
    |__""",
    # 6 ошибок - проигрыш
    """
     _______
    |/      |
    |      😵
    |      /|\\
    |      / \\
    |
    |
    |__""",
]


WORDS: list[str] = [
    "питон",
    "программа",
    "компьютер",
    "алгоритм",
    "переменная",
    "функция",
    "список",
    "словарь",
    "библиотека",
    "разработка",
]


def get_random_word() -> str:
    """Возвращение случайного слова из списка"""
    return random.choice(WORDS)


def display_word(word, guessed) -> LiteralString:
    """
    Показывает слово, заменяя неугаданные буквы на '_'

    Например: для слова "python" и угаданных букв ['p', 't']
    вернет: "p _ t _ _ _"
    """
    display = []
    for letter in word:
        if letter in guessed:
            display.append(letter)
        else:
            display.append("_")
    return " ".join(display)


def play_game() -> None:
    """Основная функция игры"""
    print('Привет! Давай сыграем в игру "Виселица"!')
    print("-" * 40)

    word: str = get_random_word()
    guessed = []
    while True:
        current_display: LiteralString = display_word(word, guessed)
        print(f"Слово: {current_display}")
        if guessed:
            print(f"Угаданные буквы: {', '.join(guessed)}")
        letter: str = input("Введите букву: ").lower()
        print("-" * 20)
        if letter in word:
            if letter in guessed:
                print(f"Буква '{letter}' уже угадана!")
            else:
                guessed.append(letter)
                print(f"✅ Отлично! Буква '{letter}' есть в слове!")
        else:
            print(f"❌ К сожалению, буквы '{letter}' нет в слове")
        won = True
        for char in word:
            if char not in guessed:
                won = False
                break
        if won:
            print(f"\n🎉 ПОЗДРАВЛЯЕМ! Вы угадали слово: {word.upper()}")
            break


def main() -> None:
    """
    Основная функция программы
    """
    print("=" * 40)
    print('         ИГРА "ВИСЕЛИЦА"')
    print("=" * 40)

    play_game()

    print("\nСпасибо за игру! До встреи!")


if __name__ == "__main__":
    main()
