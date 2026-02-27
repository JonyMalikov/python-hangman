"""
Hangman Game
Простая консольная игра "Виселица"
"""

import random

HINT_COST = 2
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


def is_russian_word(s: str) -> bool:
    """Проверяет, что строка состоит только из русских букв (включая ё)"""
    russian_alphabet = set("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    return all(char in russian_alphabet for char in s.lower())


def get_random_word() -> str:
    """Возвращение случайного слова из списка"""
    return random.choice(WORDS)


def display_word(word, guessed) -> str:
    """
    Показывает слово, заменяя неугаданные буквы на '_'

    Например: для слова "python" и угаданных букв ['p', 't']
    вернет: "p _ t _ _ _"
    """
    return " ".join([letter if letter in guessed else "_" for letter in word])


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
        print(f"Слово: {display_word(word, guessed)}")
        if wrong_letters:
            print(f"Неправильные буквы: {', '.join(wrong_letters)}")
        if guessed:
            print(f"Угаданные буквы: {', '.join(guessed)}")
        print(f"Осталось попыток: {attempts}")
        print(HANGMAN_PICS[6 - attempts])

        user_input = (
            input("\nВведите букву, слово целиком или '?' для подсказки:")
            .strip()
            .lower()
        )

        if user_input == "?":
            if attempts < HINT_COST:
                print(f"Недостаточно попыток для подсказки (нужно {HINT_COST}).")
                continue
            remaining = [c for c in word if c not in guessed]
            if not remaining:
                print("Все буквы уже открыты!")
                continue
            hint = random.choice(remaining)
            guessed.append(hint)
            attempts -= HINT_COST
            print(f"Подсказка: открыта буква '{hint}'.")
            print(f"Осталось попыток: {attempts}")
        elif len(user_input) == 1:
            if not is_russian_word(user_input):
                print("Пожалуйста, введите русскую букву.")
                continue

            if user_input in guessed or user_input in wrong_letters:
                print(f'Вы уже пробовали букву "{user_input}"!')
                continue

            if user_input in word:
                guessed.append(user_input)
                print(f"✅ Отлично! Буква '{user_input}' есть в слове!")
            else:
                wrong_letters.append(user_input)
                attempts -= 1
                print(f"❌ К сожалению, буквы '{user_input}' нет в слове")
                # print(f"Осталось попыток: {attempts}")
        else:
            if not is_russian_word(user_input):
                print("Слово должно содержать только русские буквы.")
                continue
            if user_input == word:
                guessed = list(set(word))
                print("🎉 Поздравляем! Вы угадали слово целиком!")
            else:
                attempts -= 1
                print(f"❌ Неверное слово! Осталось попыток: {attempts}")

        # won = all(char in guessed for char in word)
        if all(c in guessed for c in word):
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

    print("\nСпасибо за игру! До встречи!")


if __name__ == "__main__":
    main()
