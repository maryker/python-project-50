import pytest
from gendiff.modules.gendiff import generate_diff
from gendiff.modules.formaters.stylish import form_stylish

@pytest.fixture
def file1():
  return 'tests/fixtures/file1.json'

@pytest.fixture
def file2():
  return 'tests/fixtures/file2.json'

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

def test_json(file1, file2, result):
   assert generate_diff(file1, file2, form_stylish) == result


  
  


