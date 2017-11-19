import requests

from config import load_token
from model.scraper.util import generate_url_query, get_json_response

TOKEN = load_token()

FACEBOOK_GRAPH_BASE_URL = "https://graph.facebook.com/v2.11/"
BRUINFEED = "163576114113950"


class FeedScraper:
    def __init__(self, feed_id: str, limit: str):
        self.feed_id = feed_id
        self.limit = limit

    def get_posts(self):
        feed_response = requests.get(
            generate_url_query(self.feed_id + "/feed?limit=" + self.limit)
        )
        return get_json_response(feed_response)


feedscraper = FeedScraper(BRUINFEED, "25")
datetime = feedscraper.get_posts()
print(datetime)
