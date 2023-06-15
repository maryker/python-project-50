import pytest
from gendiff import generate_diff


f1 = open('tests/fixtures/fixture_plain.txt')
f2 = open('tests/fixtures/fixture_deep.txt')

res_plain = f1.read()
res_deep = f2.read()

f1.close()
f2.close()


@pytest.mark.parametrize("file1,file2,res",
                         [('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json', res_plain),
                          ('tests/fixtures/file1.yml',
                           'tests/fixtures/file2.yml', res_plain),
                          ('tests/fixtures/file3.json',
                           'tests/fixtures/file4.json', res_deep),
                          ('tests/fixtures/file3.yml',
                           'tests/fixtures/file4.yml', res_deep)])
def test_deep(file1, file2, res):
    assert generate_diff(file1, file2) == res
