import pytest
from gendiff.modules.gendiff import generate_diff
from tests.fixtures.fixture_plain import result


@pytest.fixture
def file1():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def file2():
    return 'tests/fixtures/file2.yml'


def test_yaml(file1, file2):
    assert generate_diff(file1, file2) == result
