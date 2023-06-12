import pytest
from gendiff.modules.gendiff import generate_diff
from tests.fixtures.fixture_deep import result


@pytest.fixture
def file3():
    return 'tests/fixtures/file3.json'


@pytest.fixture
def file4():
    return 'tests/fixtures/file4.json'


def test_deep(file3, file4):
    assert generate_diff(file3, file4) == result
