from src.model.entities import Comment


def test_creation():
    comment = Comment('Hello World', [])
    assert 'Hello World' == comment.text
