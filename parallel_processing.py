import logging
import threading
import time
from functools import partial

logger = logging.getLogger(__name__)


def countdown(num):
    for i in range(num, 0, -1):
        logger.info("%d", i)
        time.sleep(1)


def run_threading():
    func = partial(countdown, 5)
    thread = threading.Thread(target=func)

    thread.start()
    logger.info("Doing other things")
    time.sleep(3)
    logger.info("Still doing other things")

    thread.join()
    logger.info("Done")
