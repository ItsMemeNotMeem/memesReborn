import datetime
from typing import List

from model.entities import Post


class Feed:
    def __init__(self, latest_update: datetime, posts: List[Post]) -> None:
        self.latestUpdate = latest_update
        self.posts = posts
