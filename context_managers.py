import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)


class GreetingContextManager:
    def __enter__(self):
        logger.info("Hello")

    def __exit__(self, exc_type, exc_val, exc_tb):
        logger.info("Bye!")


@contextmanager
def greetings():
    logger.info("Hello")
    yield
    logger.info("Bye!")


def using_context_manager():
    with GreetingContextManager():
        logger.info("hey")

    with greetings():
        logger.info("ho")
