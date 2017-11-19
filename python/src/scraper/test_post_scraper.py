from scraper.post_scraper import PostScraper


def assert_url(expected_url, post_scraper):
    assert expected_url == post_scraper.get_picture_url()


def test_get_picture_url():
    post_scraper = PostScraper('163576114113950_359337581204468')
    assert_url(
        'https://scontent.xx.fbcdn.net/v/t1.0-9/s720x720/23561708_233623853840568_1180971634360718856_n.jpg?oh=1c5c00cb23ee188c6c6f791200f6a3a5&oe=5AA925DB',
        post_scraper
    )

test_get_picture_url()
