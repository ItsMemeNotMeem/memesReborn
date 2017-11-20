import requests

from config import load_token
from model.scraper.util import generate_url_query, get_json_response

TOKEN = load_token()

FACEBOOK_GRAPH_BASE_URL = "https://graph.facebook.com/v2.11/"
BRUINFEED = "163576114113950"


class FeedScraper:
    def __init__(self, feed_id: str, limit: int):
        self.feed_id = feed_id
        self.limit = limit

    def get_id_posts(self):
        feed_response = requests.get(
            generate_url_query(self.feed_id + "/feed?limit=" + str(self.limit))
        )
        json_posts = get_json_response(feed_response)
        return [json_post['id'] for json_post in json_posts['data']]
