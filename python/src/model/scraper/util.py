import json

from config import load_token

FACEBOOK_GRAPH_BASE_URL = "https://graph.facebook.com/v2.11/"

TOKEN = load_token()


def get_json_response(response):
    json_response = json.loads(response.content)
    if 'error' in json_response:
        error_json = json_response['error']
        raise ConnectionRefusedError(error_json['message'])
    return json_response


def generate_url_query(query):
    return FACEBOOK_GRAPH_BASE_URL + query + "&access_token=" + TOKEN
