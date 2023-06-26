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
        logger.error("Exception occurred: %s", e)
        pass
    logger.info("The tuple t = %s - contains list %s", t, l)


def dict_with_tuple_keys():

    t1 = (1,2)
    logger.info("Tuple %s can be a dict key", t1)

    d1 = {t1: 1}
    logger.info("The dict: %s", d1)

    l = [1, 2, 3]
    t2 = (1, 2, l)
    logger.info("Tuple %s can't be a dict key - list is unhashable", t2)

    try:
        d2 = {t2: 2}
    except TypeError as e:
        logger.error("Exception occurred: %s", e)

def sorted_returns_a_list():
    t = (2, 1, 3)
    logger.info("Prepared tuple %s", t)
    logger.info("Sorted tuple is %s", sorted(t))
