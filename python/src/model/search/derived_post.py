from model.entities import Post
from model.search import read_url_image_text, clean_text


class DerivedPost:
    def __init__(self, post: Post, full_text_representation: str):
        self.post = post
        self.full_text_representation = full_text_representation


def create_derived_post(post: Post) -> DerivedPost:
    image_text = read_url_image_text(post.image)
    full_text_representation = ' '.join([clean_text(post.message), clean_text(image_text)])
    return DerivedPost(post, full_text_representation)
