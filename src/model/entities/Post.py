import datetime
from typing import List

from model.entities import Comment


class Post:
    def __init__(self, text: str, image: str, comments: List[Comment], url: str,
                 datePosted: datetime, lastestUpdate: datetime):
        self.text = text
        self.image = image
        self.comments = comments
        self.url = url
        self.datePosted = datePosted
        self.lastestUpdate = lastestUpdate

