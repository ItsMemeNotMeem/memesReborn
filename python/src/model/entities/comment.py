from typing import List, Any


class Comment:
    def __init__(self, text: str, comments: List[Any]) -> None:
        self.text = text
        self.comments = comments
