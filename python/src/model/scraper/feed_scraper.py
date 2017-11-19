import json

import requests

from config import load_token
TOKEN = load_token()

FACEBOOK_GRAPH_BASE_URL = "https://graph.facebook.com/v2.11/"
BRUINFEED = "163576114113950"


def get_json_response(response):
    return json.loads(response.content)


def generate_url_query(query):
    return FACEBOOK_GRAPH_BASE_URL + query


class FeedScraper:
    def __init__(self, feed_id: str, limit: str):
        self.feed_id = feed_id
        self.limit = limit

    def get_posts(self):
        feed_response = requests.get(
            generate_url_query(BRUINFEED + "/feed?limit=" + self.limit+"&access_token=" + TOKEN)
        )
        return get_json_response(feed_response)


feedscraper = FeedScraper(BRUINFEED, "25")
datetime = feedscraper.get_posts()
print(datetime)
