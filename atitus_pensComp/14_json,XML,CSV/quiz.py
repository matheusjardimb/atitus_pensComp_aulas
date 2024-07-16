import random


def get_questions(amount: int = 10, difficulty: str = "easy") -> dict:
    """
    Alternative method, using requests, which needs to be installed with:
        pip install requests
    """
    import requests

    req = requests.get(
        f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
    )
    return req.json()


def parse_text(html_string: str) -> str:
    import html

    # Convert HTML entity to regular single quote
    return html.unescape(html_string)


def start_quiz():
    items = get_questions()["results"]  # Lista de perguntas e respostas
    score = 0
    for item_idx in range(len(items)):
        item = items[item_idx]
        correct_answer = parse_text(item["correct_answer"])

        # incorrect_answers = []
        # for x in item["incorrect_answers"]:
        #     incorrect_answers.append(parse_text(x))
        incorrect_answers = [parse_text(x) for x in item["incorrect_answers"]]

        incorrect_answers.append(correct_answer)
        print("Question:", parse_text(item["question"]))
        print("Category:", parse_text(item["category"]))
        random.shuffle(incorrect_answers)
        correct_answer_idx = None
        for answer_idx in range(len(incorrect_answers)):
            answer = incorrect_answers[answer_idx]
            print(answer_idx, "-", answer)
            if answer == correct_answer:
                correct_answer_idx = answer_idx
        answer = int(input("Type the correct answer and press enter to continue: "))
        if answer == correct_answer_idx:
            score += 1
            print("Correct!")
        else:
            print("Wrong! Correct answer:", correct_answer)
        print("Score:", score, "/", item_idx + 1)
        print("")

    print("The end!")


start_quiz()
