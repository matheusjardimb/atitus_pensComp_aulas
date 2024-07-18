def get_response(coin_a: str, coin_b: str) -> dict:
    import http.client
    import json

    conn = http.client.HTTPSConnection("api.coinbase.com")
    conn.request("GET", f"/v2/prices/{coin_a}-{coin_b}/buy")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)


def get_exchange_rate(coin_a: str, coin_b: str) -> float:
    # response = get_questions(coin_a, coin_b)
    pass


def get_new_value(coin_a: str, coin_b: str, value: float) -> float:
    pass
