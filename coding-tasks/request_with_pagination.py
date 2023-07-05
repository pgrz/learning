#!/bin/python3

# Complete the function below.
# Base url: https://jsonmock.hackerrank.com/api/movies/search/?Title=

import logging
from string import Template

import requests

url_template = Template(
    "https://jsonmock.hackerrank.com/api/movies/search/?Title=${substr}"
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def query_movie_titles(substr: str) -> list[str]:
    titles = []

    url = url_template.substitute(substr=substr)
    session = requests.Session()

    logger.info("Initialized session; will query %s", url)

    page_number = 0
    total_pages = 1

    while True:
        page_number += 1

        if page_number > total_pages:
            break

        logger.info("Getting page %s", page_number)
        page = session.get(url, params={"page": page_number}).json()
        logger.debug("Response: %s", page)

        titles.extend((result["Title"] for result in page["data"]))

        logger.info("Titles found: %d", len(titles))

        if page_number == 1:
            total_pages = page["total_pages"]
            logger.debug("Total number of pages: %d", total_pages)

    logger.info("Finishing %s", titles)

    return sorted(titles)


if __name__ == "__main__":
    assert [
        "Amazing Spiderman Syndrome",
        "Fighting, Flying and Driving: The Stunts of Spiderman 3",
        "Hollywood's Master Storytellers: Spiderman Live",
        "Italian Spiderman",
        "Spiderman",
        "Spiderman",
        "Spiderman 5",
        "Spiderman and Grandma",
        "Spiderman in Cannes",
        "Superman, Spiderman or Batman",
        "The Amazing Spiderman T4 Premiere Special",
        "The Death of Spiderman",
        "They Call Me Spiderman",
    ] == query_movie_titles("Spiderman")
    assert ["AAA, la película: Sin límite en el tiempo"] == query_movie_titles("aaa")
