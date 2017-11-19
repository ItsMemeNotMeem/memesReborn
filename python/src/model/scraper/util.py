import json

from config import load_token

FACEBOOK_GRAPH_BASE_URL = "https://graph.facebook.com/v2.11/"

TOKEN = load_token()


def get_json_response(response):
    return json.loads(response.content)


def generate_url_query(query):
    return FACEBOOK_GRAPH_BASE_URL + query + "&access_token=" + TOKEN
