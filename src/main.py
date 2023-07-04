from random import choice
from data import answer_list, sweet_list


def main():
    hello_name = input("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос!"
                       "\nКак твое имя, Божье творение?")
    print(f"Привет, {hello_name}!")
    while True:
        question = input("Задавай свой вопрос, но бойся! Ответ может быть обескураживающим }:D")
        print(choice(answer_list))
        print(f"Хочешь ещё что-нибудь спросить, {choice(sweet_list)}?")