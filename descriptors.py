import logging

logger = logging.getLogger(__name__)


class DirectoryNameLength:
    def __get__(self, obj, objtype=None):
        return len(obj.name)


class Directory:
    def __init__(self, name: str):
        self.name = name

    name_length = DirectoryNameLength()


class Person:
    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name

    @property
    def name(self):
        return " ".join((self._first_name, self._last_name))

    name_length = DirectoryNameLength()


def run_with_descriptor():
    directory = Directory(name="asdf")
    logger.info(
        "Directory %s has a name length of %d", directory, directory.name_length
    )
    person = Person(first_name="Bill", last_name="Cosby")
    logger.info("Person %s has a name length of %d", person, person.name_length)
