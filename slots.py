import logging
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


class MyClass:
    __slots__ = "a"


@dataclass(slots=True)
class MyDataclass:
    a: int = field(init=False, default=0)


def run_with_slots():
    for kls in [MyClass, MyDataclass]:
        o = kls()
        logger.info("Created object %s", o)
        o.a = 1
        try:
            logger.info("Trying to modify attribute b")
            o.b = 2
        except AttributeError as e:
            logger.error("Exception encountered: %s", e)
