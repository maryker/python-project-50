import pytest
from hexlet_code.modules.generate_diff import generate_diff
from hexlet_code.modules.formater import stylish

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
  assert stylish(generate_diff(file1, file2)) == result