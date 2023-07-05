import logging
import string
from collections import defaultdict

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger()


def _parts_histogram(parts: list[str]) -> dict[str, int]:
    histogram = defaultdict(int)

    for part in parts:
        histogram[part] += 1

    return dict(histogram)


def check_subphrase(subphrase: str, word_parts: list[str]) -> bool:
    logger.debug("Checking %s against %s", subphrase, word_parts)

    window_size = len(word_parts[0])

    phrase_parts = [
        subphrase[i : i + window_size] for i in range(0, len(subphrase), window_size)
    ]
    logger.debug("Chunked into %s", phrase_parts)

    subphrase_part_histogram = _parts_histogram(phrase_parts)
    query_part_histogram = _parts_histogram(word_parts)

    logger.debug("Histogram of the subphrase %s", subphrase_part_histogram)
    logger.debug("Histogram of the query %s", query_part_histogram)

    return subphrase_part_histogram == query_part_histogram


def find_word_parts_indices(phrase: str, word_parts: list[str]) -> list[int]:
    """
    phrase: a string
    word_parts: a list of strings that are all the same length (length is non-0)

    Find all starting indices in phrase, that are a concatenation* of every string in word_parts

    *Note: a concatenation has each string from word_parts exactly once without any intervening characters
    """

    concatenated_word_parts_length = len("".join(word_parts))

    results = []

    for i, _ in enumerate(phrase):
        subphrase = phrase[i : i + concatenated_word_parts_length]

        if len(subphrase) < concatenated_word_parts_length:
            break

        if check_subphrase(subphrase=subphrase, word_parts=word_parts):
            results.append(i)

    return results


# ------------------ test cases ---------------------------


def run_test_case(test_id, phrase, word_parts, expected_indices):
    print("=" * 50)
    indices = find_word_parts_indices(phrase, word_parts)

    if indices == expected_indices:
        print(f"Test case #{test_id}: Passed ✅")
    else:
        print(f"Test case #{test_id}: Failed ❌")
        print(f"Phrase: {phrase}")
        print(f"Word parts: {word_parts}")
        print(f"Expected {expected_indices} but got {indices}")


run_test_case(
    test_id=0,
    phrase="blabarfoothefoobarman1",
    word_parts=["foo", "bar"],
    expected_indices=[3, 12],
)

run_test_case(
    test_id=0.1,
    phrase="blabarXfoothefoobarman",
    word_parts=["foo", "bar"],
    expected_indices=[13],
)

run_test_case(
    test_id=1,
    phrase="aaaa",
    word_parts=["a", "a"],
    expected_indices=[0, 1, 2],
)

run_test_case(
    test_id=2,
    phrase="bbarfoothefoobarman",
    word_parts=["foo", "bar"],
    expected_indices=[1, 10],
)

run_test_case(
    test_id=3,
    phrase="aaa",
    word_parts=["a", "a", "a"],
    expected_indices=[0],
)

run_test_case(
    test_id=4,
    phrase="aaaa",
    word_parts=["a", "a", "a"],
    expected_indices=[0, 1],
)

run_test_case(
    test_id=5,
    phrase="barfooqwertyuiopasdfghjklzxcvbnmfoobar",
    word_parts=list(string.ascii_lowercase),
    expected_indices=[6],
)

run_test_case(
    test_id=6,
    phrase="bfoofofoob",
    word_parts=["ofo", "foo"],
    expected_indices=[3],
)

run_test_case(
    test_id=7,
    phrase="acbcaabbbaacabba",
    word_parts=["a", "a", "b"],
    expected_indices=[4, 8],
)

run_test_case(
    test_id=8,
    phrase="barbarfoodoo",
    word_parts=["foo", "bar", "doo"],
    expected_indices=[3],
)
