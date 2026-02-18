"""
Hangman Game
Простая консольная игра "Виселица"
"""

import random

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


def display_word(word, guessed) -> str:
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
    wrong_letters = []
    attempts = 6

    print(f"У Вас есть {attempts} попыток.")
    print(HANGMAN_PICS[0])
    while True:
        print("\n" + "=" * 40)

        current_display = display_word(word, guessed)
        print(f"Слово: {current_display}")

        if wrong_letters:
            print(f"Неправельные буквы: {', '.join(wrong_letters)}")
        if guessed:
            print(f"Угаданные буквы: {', '.join(guessed)}")

        print(f"Осталось попыток: {attempts}")
        print(HANGMAN_PICS[6 - attempts])

        letter: str = input("Введите букву: ").lower()

        if len(letter) != 1:
            print("Пожалуйста, введите только одну букву!")
            continue
        if letter in guessed or letter in wrong_letters:
            print(f'Вы уже пробовали букву "{letter}"!')
            continue

        if letter in word:
            guessed.append(letter)
            print(f"✅ Отлично! Буква '{letter}' есть в слове!")
        else:
            wrong_letters.append(letter)
            attempts -= 1
            print(f"❌ К сожалению, буквы '{letter}' нет в слове")
            print(f"Осталось попыток: {attempts}")

        won = all(char in guessed for char in word)
        if won:
            print("\n" + "=" * 40)
            print(HANGMAN_PICS[6 - attempts])
            print(f"\n🎉 ПОЗДРАВЛЯЕМ! Вы угадали слово: {word.upper()}")
            print(f"У Вас осталось {attempts} попыток.")
            break

        if attempts <= 0:
            print("\n" + "=" * 40)
            print(HANGMAN_PICS[6])
            print("💀 ИГРА ОКОНЧЕНА! Вы проиграли.")
            print(f"Загаданное слово было: {word.upper()}")
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
