import random


def ask_questions(questions, num_questions=5):
    correct_answers = 0

    for _ in range(num_questions):
        question = random.choice(list(questions))

        answer = get_user_answer(question, questions[question])

        if answer == questions[question]:
            correct_answers += 1

        questions.pop(question)

    return correct_answers


def get_user_answer(question, correct_answer):
    user_input = input(question).lower().replace(".", "").replace(" ", "").strip()
    return user_input


def main():
    questions = {
        "What is the capital of France?: ": "paris",
        "How many planets are there in the solar system?: ": "8",
        "Which ocean is the largest on Earth?: ": "pacific",
        'Who wrote the book "Harry Potter"?: ': "jkrowling",
        "How many players are there in a standard soccer team?: ": "11",
        "Which continent is the largest?: ": "asia",
        "How many seasons are there?: ": "4",
        "Who is the author of the famous painting Mona Lisa?: ": "leonardodavinci",
        "What is the chemical symbol for copper?: ": "cu",
        "How many seconds are in a minute?: ": "60",
    }

    num_correct_answers = ask_questions(questions)

    print(f"You answered {num_correct_answers} out of 5 questions correctly!")


if __name__ == "__main__":
    main()
