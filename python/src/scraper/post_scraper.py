import json
import os
from urllib.request import urlopen

import requests

from model.entities import Post

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
        return get_json_response(picture_response)

    def get_date_posted(self):
        object_id = self.__get_obj_id()
        date_posted = requests.get(
            FACEBOOK_GRAPH_BASE_URL + object_id + "?fields=created_time&access_token=" + TOKEN
        )
        return get_json_response(date_posted)['created_time']

    def get_updated_time(self):
        object_id = self.__get_obj_id()
        date_posted = requests.get(
            FACEBOOK_GRAPH_BASE_URL + object_id + "?fields=updated_time&access_token=" + TOKEN
        )
        return get_json_response(date_posted)['updated_time']

    def get_post_obj(self):
        post_obj = Post("", self.get_picture_url(), self.get_comments(), self.get_picture_url(),
                        self.get_date_posted(), self.get_updated_time())
        return post_obj
