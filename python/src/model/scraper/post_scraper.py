from typing import List
from urllib.request import urlopen

import requests

from model.entities import Post
from model.scraper.util import get_json_response, generate_url_query


class PostScraper:
    def __init__(self, post_id: str):
        self.post_id = post_id
        self.object_id = self.__get_obj_id()

    def __get_obj_id(self):
        obj_response = requests.get(
            generate_url_query(self.post_id + "?fields=object_id")
        )
        object_id_json = get_json_response(obj_response)
        return object_id_json['object_id']

    def __fetch_json_response(self, id_code: str, attribute: str):
        response = requests.get(
            generate_url_query("{}?fields={}".format(id_code, attribute))
        )
        return get_json_response(response)

    def __fetch_content_or_nil(self, id_code: str, attribute):
        json_response = self.__fetch_json_response(id_code, attribute)
        return json_response[attribute] if attribute in json_response else ''

    def get_picture_url(self):
        api_url = generate_url_query(self.object_id + "/picture?type=normal")
        return urlopen(api_url).geturl()

    def get_comments(self):
        return self.__fetch_json_response(self.object_id, 'comments')

    def get_date_posted(self):
        return self.__fetch_content_or_nil(self.object_id, 'created_time')

    def get_updated_time(self):
        return self.__fetch_content_or_nil(self.object_id, 'updated_time')

    def get_message(self):
        return self.__fetch_content_or_nil(self.post_id, 'message')

    def get_post_obj(self):
        return Post(
            self.get_message(),
            self.get_picture_url(),
            self.get_comments(),
            self.get_picture_url(),
            self.get_date_posted(),
            self.get_updated_time()
        )


def create_eligible_post_scrapers(post_ids: List[str]) -> List[PostScraper]:
    post_scrapers = []
    for post_id in post_ids:
        try:
            post_scrapers.append(PostScraper(post_id))
        except KeyError:
            pass
    return post_scrapers
