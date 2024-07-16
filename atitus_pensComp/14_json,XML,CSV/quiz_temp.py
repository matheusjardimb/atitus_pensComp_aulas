def get_questions(amount: int = 10, difficulty: str = "easy") -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("opentdb.com")
    conn.request(
        "GET", f"/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
    )
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def get_questions_alternative(amount: int = 10, difficulty: str = "easy") -> dict:
    """
    Alternative method, using requests, which needs to be installed with:
        pip install requests
    """
    import requests

    req = requests.get(
        f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
    )
    return req.json()


print(get_questions(2))
# print(get_questions_alternative())
