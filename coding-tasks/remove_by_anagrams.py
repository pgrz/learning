import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger()


def _calculate_hash(word: str) -> int:
    thehash = hash("".join(sorted(word)))
    logger.debug("%s: %d", word, thehash)
    return thehash


def remove_by_anagrams(text: list[str]) -> list[str]:
    hashed_words: dict[int, str] = {}

    for word in text:
        word_hash = _calculate_hash(word=word)

        if hashed_words.get(word_hash, None):
            logger.warning("Omitting %s - hash already found", word)
        else:
            logger.info("Adding %s with hash %d", word, word_hash)

            hashed_words[word_hash] = word

    logger.info("Kept %d words", len(hashed_words))

    return sorted([val for val in hashed_words.values()])


if __name__ == "__main__":
    assert ["abab"] == remove_by_anagrams(["abab", "abba", "baba"])
    assert ["foo"] == remove_by_anagrams(["foo", "oof"])
