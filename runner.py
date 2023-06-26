#!/usr/bin/env python3
import logging

import context_managers
import decorators
import default_value
import generators
import parallel_processing
import quirks

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


funcs_to_run = (
    context_managers.using_context_manager,
    decorators.run_decorated,
    default_value.run_add_value,
    generators.run_generator,
    parallel_processing.run_threading,
    quirks.assign_and_modify_in_tuple,
    quirks.sorted_returns_a_list,
)

if __name__ == "__main__":
    for func in funcs_to_run:
        logger.info("Running function %s", func.__name__)
        func()
        logger.info("Done!\n")
