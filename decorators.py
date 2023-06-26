import logging
import time
from functools import wraps
from typing import Callable

logger = logging.getLogger(__name__)


def arg_decorator(character):
    def _arg_decorator(func: Callable) -> Callable:
        @wraps(func)
        def _wrapped_func(*args, **kwargs):
            start_time = time.time()

            result = func(*args, **kwargs)

            end_time = time.time()
            duration = end_time - start_time

            print(
                "%s Args: %s, kwargs: %s, result: %s, time: %s s %s"
                % (character, args, kwargs, result, duration, character)
            )
            return result

        return _wrapped_func

    return _arg_decorator


@arg_decorator("#")
def foo(x):
    return x * 2


def run_decorated():
    logger.info("Running foo with 5")
    foo(5)
