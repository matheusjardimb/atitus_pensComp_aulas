def get_movies(texto_busca: str) -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("search.imdbot.workers.dev")
    conn.request("GET", f"/?q={texto_busca}")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def print_movie(movie: dict) -> None:
    print(movie["#AKA"])
    print("\tRank: #", movie["#RANK"])
    print("\tActors: ", movie["#ACTORS"])
    print("\tIMDB: ", movie["#IMDB_URL"])
    print("\tPoster: ", movie["#IMG_POSTER"])


busca = input("Digite o nome do filme: ")
movies = get_movies(busca)

for movie in movies["description"]:
    print_movie(movie)
    print()
