import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)


def add_value(value: Any, thelist: Optional[list] = None):
    actual_list = thelist if thelist else []
    actual_list.append(value)
    return actual_list


def run_add_value():
    l1 = add_value("value")
    l2 = add_value("another value")
    l3 = []
    l4 = add_value(8, l3)
    l5 = add_value(15, l2)

    logger.info("Lists: %s, %s, %s, %s, %s", l1, l2, l3, l4, l5)
