from model.scraper.feed_scraper import FeedScraper
from model.scraper.post_scraper import create_eligible_post_scrapers
from model.search.derived_post import create_derived_post
from model.search.indexer import Indexer

INDEX_DIR = "../data/indices"

BRUINFEED_ID = "163576114113950"


def test_index():
    feedscraper = FeedScraper(BRUINFEED_ID, 25)
    post_ids = feedscraper.get_id_posts()
    post_scrapers = create_eligible_post_scrapers(post_ids)
    posts = []
    for index, post_scraper in enumerate(post_scrapers):
        print('printed {0} id: {1}'.format(index, post_scraper.post_id))
        posts.append(post_scraper.get_post_obj())
    print('indexing data')
    derived_posts = [create_derived_post(post) for post in posts]
    indexer = Indexer(INDEX_DIR)
    indexer.index(derived_posts)


test_index()
