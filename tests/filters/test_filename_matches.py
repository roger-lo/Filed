import pytest

from src.filters.filename_matches import FilenameMatches


@pytest.fixture
def filterable():
    return FilenameMatches()


def test_zero_matches(filterable):
    files = ["foo.py", "bar.py"]
    regex = ".*\.txt"
    result = []
    print(filterable.filter(files, regex), result)
    assert filterable.filter(files, regex) == result


def test_single_match(filterable):
    files = ["foo.txt", "bar.py"]
    regex = ".*\.txt"
    result = ["foo.txt"]
    assert filterable.filter(files, regex) == result


def test_multiple_matches(filterable):
    files = ["foo.txt", "bar.txt"]
    regex = ".*\.txt"
    result = ["foo.txt", "bar.txt"]
    assert filterable.filter(files, regex) == result

