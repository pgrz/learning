import logging
from functools import reduce
from operator import add

logger = logging.getLogger(__name__)


# TODO: Add generator send example


def generate_divisable_by_3_or_7(n):
    logger.info("Creating a generator for %d", n)
    num = 1
    while num <= n:
        if num % 3 == 0 or num % 7 == 0:
            yield num
        num += 1


def print_generator(gen):
    for val in gen:
        logger.info("Got %s from generator", val)


def run_generator():
    gen = generate_divisable_by_3_or_7(8)
    print_generator(gen)

    gen = generate_divisable_by_3_or_7(20)
    logger.info("Filtering the generator >= 14")
    filtered_gen = filter(lambda x: x >= 14, gen)
    print_generator(filtered_gen)

    gen = generate_divisable_by_3_or_7(8)
    logger.info("Sum of the generator using reduce: %d", reduce(add, gen))
    logger.info("Can't use sum, because it accepts iterable - reduce works pairwise")
