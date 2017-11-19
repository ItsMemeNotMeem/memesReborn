import json
from urllib.request import urlopen

import requests

from config import load_token
from model.entities import Post
TOKEN = load_token()

FACEBOOK_GRAPH_BASE_URL = "https://graph.facebook.com/v2.11/"


def get_json_response(response):
    return json.loads(response.content)


def generate_url_query(query):
    return FACEBOOK_GRAPH_BASE_URL + query


class PostScraper:
    def __init__(self, post_id: str):
        self.post_id = post_id

    def __get_obj_id(self):
        obj_response = requests.get(
            generate_url_query(self.post_id + "?fields=object_id&access_token=" + TOKEN)
        )
        return get_json_response(obj_response)['object_id']

    def get_picture_url(self):
        object_id = self.__get_obj_id()
        query = object_id + "/picture?access_token=" + TOKEN + "&type=normal"
        api_url = generate_url_query(query)

        return urlopen(api_url).geturl()

    def get_comments(self):
        object_id = self.__get_obj_id()
        picture_response = requests.get(
            generate_url_query(object_id + "?fields=comments&access_token=" + TOKEN)
        )
        return get_json_response(picture_response)

    def get_date_posted(self):
        object_id = self.__get_obj_id()
        date_posted = requests.get(
            generate_url_query(object_id + "?fields=created_time&access_token=" + TOKEN)
        )
        return get_json_response(date_posted)['created_time']

    def get_updated_time(self):
        object_id = self.__get_obj_id()
        date_posted = requests.get(
            generate_url_query(object_id + "?fields=updated_time&access_token=" + TOKEN)
        )
        return get_json_response(date_posted)['updated_time']

    def get_post_obj(self):
        post_obj = Post("", self.get_picture_url(), self.get_comments(), self.get_picture_url(),
                        self.get_date_posted(), self.get_updated_time())
        return post_obj
