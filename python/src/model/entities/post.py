import datetime
from typing import List

from model.entities import Comment


class Post:
    def __init__(self, message: str, image: str, comments: List[Comment], url: str,
                 date_posted: datetime, latest_update: datetime):
        self.message = message
        self.image = image
        self.comments = comments
        self.url = url
        self.date_posted = date_posted
        self.latest_update = latest_update
