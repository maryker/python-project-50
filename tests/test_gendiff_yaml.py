import pytest
from gendiff.modules.gendiff import generate_diff


@pytest.fixture
def file1():
    return 'tests/fixtures/file1.yml'


@pytest.fixture
def file2():
    return 'tests/fixtures/file2.yml'


@pytest.fixture
def result():
    return '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


def test_yaml(file1, file2, result):
    assert generate_diff(file1, file2) == result
