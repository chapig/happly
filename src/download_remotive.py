import feedparser
from bs4 import BeautifulSoup


def get_jobs(query):
    """
    Get jobs from remotive.com
    :param query: A string representing the search query.
    :return: A list of job postings.
    """

    # Replace spaces with %20 for the query
    query = query.replace(' ', '%20')
    url = f'https://remotive.com/remote-jobs/feed?query={query}'
    feed = feedparser.parse(url)

    jobs = []

    for entry in feed.entries:
        job = {
            'title': entry.title,
            'link': entry.link,
            'published:': entry.published,
            'description': BeautifulSoup(entry.description, 'html.parser').get_text(),
            'company': entry.author,
            'tags': entry.tags
        }

        jobs.append(job)

    return jobs
