def get_questions(amount: int = 10, difficulty: str = 'easy') -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("opentdb.com")
    conn.request("GET", f"/api.php?amount={amount}&difficulty={difficulty}&type=multiple")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def parse_text(html_string: str) -> str:
    import html

    # Convert HTML entity to regular single quote
    return html.unescape(html_string)


def start_quiz():
    pass


start_quiz()
