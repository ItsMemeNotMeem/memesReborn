import json
import os
from urllib.request import urlopen

import requests

TOKEN = os.environ.get('FACEBOOK_TEMP_TOKEN')

FACEBOOK_GRAPH_BASE_URL = "https://graph.facebook.com/v2.11/"


def get_json_response(response):
    return json.loads(response.content)


class PostScraper:
    def __init__(self, post_id: str):
        self.post_id = post_id

    def __get_obj_id(self):
        obj_response = requests.get(
            FACEBOOK_GRAPH_BASE_URL + self.post_id + "?fields=object_id&access_token=" + TOKEN
        )
        return get_json_response(obj_response)['object_id']

    def get_picture_url(self):
        object_id = self.__get_obj_id()
        api_url = FACEBOOK_GRAPH_BASE_URL + object_id + "/picture?access_token=" + TOKEN + "&type=normal"
        return urlopen(api_url).geturl()

    def get_comments(self):
        object_id = self.__get_obj_id()
        picture_response = requests.get(
            FACEBOOK_GRAPH_BASE_URL + object_id + "?fields=comments&access_token=" + TOKEN
        )
        print(get_json_response(picture_response))
