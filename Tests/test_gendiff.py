import pytest
from gendiff.gendiff import generate_diff

JSON1 = 'file1.json'
JSON2 = 'file2.json'
YAML1 = 'file1.yml'
YAML2 = 'file2.yml'
NESTED_JSON1 = 'filepath1.json'
NESTED_JSON2 = 'filepath2.json'
NESTED_YAML1 = 'filepath1.yml'
NESTED_YAML2 = 'filepath2.yml'

FLAT_STYLISH = 'Tests/Fixtures/Results/flat_stylish.txt'
NESTED_STYLISH = 'Tests/Fixtures/Results/nested_stylish.txt'

@pytest.mark.parametrize('file1, file2, expected', [
    (JSON1, JSON2, FLAT_STYLISH),
    (YAML1, YAML2, FLAT_STYLISH),
    (NESTED_JSON1, NESTED_JSON2, NESTED_STYLISH),
    (NESTED_YAML1, NESTED_YAML2, NESTED_STYLISH)
])

def test_gendiff(file1, file2, expected):
    with open(expected) as file:
        expected_result = file.read()
    assert generate_diff(file1, file2) == expected_result