import pytest
from hexlet_code.modules.generate_diff import generate_diff
from hexlet_code.modules.formater import stylish

@pytest.fixture
def file3():
  return 'tests/fixtures/file3.json'

@pytest.fixture
def file4():
  return 'tests/fixtures/file4.json'


@pytest.fixture
def result():
  return '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


def test_deep(file3, file4, result):
  assert stylish(generate_diff(file3, file4)) == result