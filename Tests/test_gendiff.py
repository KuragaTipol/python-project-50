import pytest
from gendiff.gendiff import generate_diff

JSON1 = 'file1.json'
JSON2 = 'file2.json'

RESULT = 'Tests/Fixtures/result.txt'

@pytest.mark.parametrize('file1, file2, expected', [
    (JSON1, JSON2, RESULT)
])

def test_gendiff(file1, file2, expected):
    with open(expected) as file:
        expected_result = file.read()
    assert generate_diff(file1, file2) == expected_result