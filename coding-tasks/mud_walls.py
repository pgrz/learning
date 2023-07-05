#!/bin/python3
#
# Complete the 'maxHeight' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
# 1. INTEGER_ARRAY wallPositions
# 2. INTEGER_ARRAY wallHeights
#

import logging


# Log level is set to ERROR to disable logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger()


def _build_mud_wall(gap_size: int, left_height: int, right_height: int) -> int:
    height_difference = abs(left_height - right_height)

    logger.debug("Gap size: %d, height difference: %d", gap_size, height_difference)

    if gap_size <= height_difference:
        size_increment = gap_size
    else:
        if left_height != right_height:
            logger.debug("Running wall builder against same-sized walls")

            walls_height = max((left_height, right_height))
            new_gap_size = gap_size - height_difference

            return _build_mud_wall(
                gap_size=new_gap_size,
                left_height=walls_height,
                right_height=walls_height,
            )

        else:
            logger.debug("Searching for the middle")

            gap_odd_sized = bool(gap_size % 2 == 1)
            size_increment = int(gap_size / 2) + int(gap_odd_sized)

    max_heights = (left_height + size_increment, right_height + size_increment)

    logger.debug("Max heights: %s; size_increment: %d", max_heights, size_increment)

    return min(max_heights)


def maxHeight(wallPositions: list[int], wallHeights: list[int]) -> int:
    # Write your code here

    max_mud_height = 0
    current_position = None
    current_height = None

    for next_position, next_height in zip(wallPositions, wallHeights):
        logger.info(
            "Processing walls %s:%s and %d:%d; current max height: %d",
            current_position,
            current_height,
            next_position,
            next_height,
            max_mud_height,
        )

        if not current_position:
            logger.debug("First iteration; getting next wall")

        elif next_position == current_position + 1:
            logger.debug(
                "The walls at %d and %d are adjacent; skipping",
                current_position,
                next_position,
            )

        else:
            logger.debug("Building a mud wall")

            current_max_mud_height = _build_mud_wall(
                gap_size=next_position - current_position - 1,
                left_height=current_height,
                right_height=next_height,
            )

            max_mud_height = max((current_max_mud_height, max_mud_height))

        current_position = next_position

        current_height = next_height

    logger.info("Max mud height: %d", max_mud_height)

    return max_mud_height


if __name__ == "__main__":
    assert 0 == maxHeight([1, 2], [1, 1])

    assert 2 == maxHeight([1, 3], [1, 1])
    assert 2 == maxHeight([1, 4], [1, 1])
    assert 3 == maxHeight([1, 5], [1, 1])

    assert 4 == maxHeight([1, 5], [1, 5])
    assert 55 == maxHeight([1, 100], [1, 10])
