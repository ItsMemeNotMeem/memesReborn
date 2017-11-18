import datetime
from typing import List

from model.entities import Post


class Feed:
    def __init__(self, lastestUpdate: datetime, posts: List[Post]) -> None:
        self.lastestUpdate = lastestUpdate
        self.posts = posts
