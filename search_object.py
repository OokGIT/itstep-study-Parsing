import requests

# URL для поиска и хидеры. Это из прошлого ДЗ ))
URL = 'https://6112b58389c6d00017ac04f1.mockapi.io/new_res'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:90.0) Gecko/20100101 Firefox/90.0',
           'accept': '*/*'}

# Тут две переменные - искомый ключ и его значение
SEARCH_KEY = 'res'
SEARCH_VALUE = 'ok'

response = requests.get(URL).json()[0]


# Тот самый рекурсивнй перебор =)
def find_object(obj, key):
    if key in obj:
        return obj[key]
    for k, v in obj.items():
        if isinstance(v, dict):
            item = find_object(v, key)
            if item is not None:
                return item
        elif isinstance(v, list):
            for list_item in v:
                item = find_object(list_item, key)
                if item is not None:
                    return item


if find_object(response, SEARCH_KEY) is None:
    print("Мы вообще не нашли ключ", SEARCH_KEY, "в выводе")
elif (find_object(response, SEARCH_KEY)) == SEARCH_VALUE:
    print("Ура!!! Ключ", SEARCH_KEY, "со значением", SEARCH_VALUE, "найден!")
else:
    print("Ключ", SEARCH_KEY, "найден но его значение -", find_object(response, SEARCH_KEY))
