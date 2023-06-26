import logging

logger = logging.getLogger(__name__)


def assign_and_modify_in_tuple():
    l = [1, 2]
    t = (l, 3, 4)
    logger.info("Prepared a tuple t = %s - contains list %s", t, l)
    try:
        logger.info("Trying to modify t[0]")
        t[0] += [7]
    except TypeError as e:
        logger.error("Exception occured: %s", e)
        pass
    logger.info("The tuple t = %s - contains list %s", t, l)


def sorted_returns_a_list():
    t = (2, 1, 3)
    logger.info("Prepared tuple %s", t)
    logger.info("Sorted tuple is %s", sorted(t))
