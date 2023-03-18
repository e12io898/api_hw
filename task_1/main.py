import requests

def super(hero_list: list):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response, buffer = requests.get(url), []
    for superhero in response.json():
        if superhero['name'] in hero_list:
            buffer.append([superhero["name"],
                           superhero['powerstats']['intelligence']])
    sort_buffer = sorted(buffer, key=lambda x: x[1], reverse=True)
    return sort_buffer[0][0]

print(super(['Hulk', 'Captain America', 'Thanos']))