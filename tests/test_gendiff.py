import pytest
from gendiff import generate_diff


@pytest.mark.parametrize("file1,file2,result",
                         [('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json', 'tests/fixtures/fixture_plain.txt'),
                          ('tests/fixtures/file1.yml',
                           'tests/fixtures/file2.yml', 'tests/fixtures/fixture_plain.txt'),
                          ('tests/fixtures/file3.json',
                           'tests/fixtures/file4.json', 'tests/fixtures/fixture_deep.txt'),
                          ('tests/fixtures/file3.yml',
                           'tests/fixtures/file4.yml', 'tests/fixtures/fixture_deep.txt')])
def test_deep(file1, file2, result):
    with open(result, 'r') as res:
        assert generate_diff(file1, file2) == res.read()
