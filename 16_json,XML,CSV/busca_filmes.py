def get_movies(texto_busca: str) -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("search.imdbot.workers.dev")
    conn.request("GET", f"/?q={texto_busca}")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def search_movie(movie_name: dict) -> dict:
    pass
