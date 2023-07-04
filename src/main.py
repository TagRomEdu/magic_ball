from random import choice
from data import answer_list, sweet_list, another_list


def main():
    hello_name = input("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос!"
                       "\nКак твое имя, Божье творение?")
    print(f"Привет, {hello_name}!")
    while True:
        question = input(f"{choice(another_list)}")
        print(choice(answer_list))
        another_question = input(f"Хочешь ещё что-нибудь спросить, {choice(sweet_list)}?")
        if another_question.lower() != 'да':
            print("Давай, проваливай! Всего хорошего.")
            break


if __name__ == "__main__":
    main()
