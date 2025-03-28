from collections import Counter

import pytest

from top_words_counter import clean_text, count_words, get_top_words


@pytest.fixture
def sample_text():
    return "Hello, world! Hello everyone. This is a test text. Test text sample."


def test_clean_text(sample_text):
    cleaned = clean_text(sample_text)
    assert cleaned == "hello world hello everyone this is a test text test text sample"


@pytest.mark.parametrize(
    "text,expected_count",
    [
        ("hello hello world", Counter({"hello": 2, "world": 1})),
        ("test test test", Counter({"test": 3})),
    ],
)
def test_count_words(text, expected_count):
    assert count_words(text) == expected_count


def test_get_top_words():
    word_counts = Counter({"hello": 3, "world": 2, "test": 1})
    top_words = get_top_words(word_counts, 2)
    assert top_words == [("hello", 3), ("world", 2)]
