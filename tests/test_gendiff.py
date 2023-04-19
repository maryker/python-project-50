import pytest
import json
from hexlet_code.scripts.gendiff import generate_diff

@pytest.fixture
def file1():
  return 'tests/fixtures/file1.json'

@pytest.fixture
def file2():
  return 'tests/fixtures/file2.json'

@pytest.fixture
def result():
  return '''{
 + empty: 
 - follow: false
   host: hexlet.io
 + name: null
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: true
}'''


def test_gendiff(file1, file2, result):
  assert generate_diff(file1, file2) == result
  
  


