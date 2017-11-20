import os
from typing import List

from whoosh.fields import Schema, TEXT
from whoosh.index import create_in, open_dir

from model.search.derived_post import DerivedPost

FULL_TEXT_REPRESENTATION_FIELD = 'full_text_representation'


class Indexer:
    def __init__(self, index_file_path) -> None:
        schema = Schema(**{FULL_TEXT_REPRESENTATION_FIELD: TEXT})
        # TODO may have to load indexer rather than create it
        # TODO create a make of this
        if not os.path.exists(index_file_path):
            os.makedirs(index_file_path)
            self.indexer = create_in(index_file_path, schema)
        else:
            self.indexer = open_dir(index_file_path)
        self.index_writer = self.indexer.writer()

    def index(self, posts: List[DerivedPost]):
        for post in posts:
            self.index_writer.add_document(post.full_text_representation)
        self.index_writer.commit()
