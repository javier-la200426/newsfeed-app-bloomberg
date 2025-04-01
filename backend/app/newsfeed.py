#OG
# """Module for retrieving newsfeed information."""

# from dataclasses import dataclass
# from datetime import datetime


# @dataclass
# class Article:
#     """Dataclass for an article."""

#     author: str
#     title: str
#     body: str
#     publish_date: datetime
#     image_url: str
#     url: str


# def get_all_news() -> list[Article]:
#     """Get all news articles from the datastore."""
#     # 1. Use Redis client to fetch all articles
#     # 2. Format the data into articles
#     # 3. Return a list of the articles formatted 
#     print("hello worlds")
#     return []


# def get_featured_news() -> Article | None:
#     """Get the featured news article from the datastore."""
#     # 1. Get all the articles
#     # 2. Return as a list of articles sorted by most recent date
#     return None


"""Module for retrieving newsfeed information."""

from dataclasses import dataclass
from datetime import datetime
from app.utils.redis import REDIS_CLIENT



@dataclass
class Article:
    """Dataclass for an article."""

    author: str
    title: str
    body: str
    publish_date: datetime
    image_url: str
    url: str


def format_article(article_data: dict) -> Article:
    """Convert raw article dictionary into an Article object."""
    return Article(
        author=article_data["author"],
        title=article_data["title"],
        body=article_data["text"],  # 'body' is stored as 'text'
        publish_date= datetime.fromisoformat(article_data["published"]),
        image_url=article_data["thread"]["main_image"],
        url=article_data["url"]
    )


def get_all_news() -> list[Article]:
    """Get all news articles from the datastore."""
    # 1. Use Redis client to fetch all articles
    raw_articles = REDIS_CLIENT.get_entry("all_articles")
    if not raw_articles:
        return []
    # 2. Format the data into articles
    # 3. Return a list of the articles formatted 

    return [format_article(article_data) for article_data in raw_articles]



def get_featured_news() -> Article | None:
    """Get the featured news article from the datastore."""
    # 1. Get all the articles
    articles = get_all_news()
    if not articles:
        return None
    # 2. Return as a list of articles sorted by most recent date
    articles.sort(key=lambda a: a.publish_date, reverse=True)

    return articles[1]
