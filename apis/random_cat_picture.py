import requests
import os

api_key = os.environ['API_CATS']


class Cats:
    def __init__(self):
        self.url = 'https://api.thecatapi.com/v1/images/search'
        # authenticate
        self.auth_header = {'x-api-key':api_key}
        # get jpg, png and gif
        self.r = requests.get(self.url + '?mime_types=jpg,png', self.auth_header)
        self.r_gif = requests.get(self.url + '?mime_types=gif', self.auth_header)

    def cat_url(self):
        if self.r.status_code == 200:
            return self.r.json()[0]['url']
        else:
            return 'Meow! I\'m having hard time communicating with cat server. Please try later!'


    def cat_gif_url(self):
        if self.r_gif.status_code == 200:
            return self.r_gif.json()[0]['url']
        else:
            return 'Meow! I\'m having hard time communicating with cat server. Please try later!'
Cats()
