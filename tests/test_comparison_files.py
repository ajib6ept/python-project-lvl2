import json
import os

import pytest
from gendiff.cli import generate_diff

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), "fixtures")

PATH_FLAT_JSON_FILE1 = "./tests/fixtures/flat_file1.json"
PATH_FLAT_JSON_FILE2 = "./tests/fixtures/flat_file2.json"

PATH_FLAT_YAML_FILE1 = "./tests/fixtures/flat_file1.yml"
PATH_FLAT_YAML_FILE2 = "./tests/fixtures/flat_file2.yml"

PATH_NESTED_JSON_FILE1 = "./tests/fixtures/nested_file1.json"
PATH_NESTED_JSON_FILE2 = "./tests/fixtures/nested_file2.json"

PATH_NESTED_YAML_FILE1 = "./tests/fixtures/nested_file1.yml"
PATH_NESTED_YAML_FILE2 = "./tests/fixtures/nested_file2.yml"


DEFAULT_COMPARISON_PARAMETRS = [
    (
        (PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2),
        "expected_comparison_flat_files_stylish.txt",
    ),
    (
        (PATH_FLAT_YAML_FILE1, PATH_FLAT_YAML_FILE2),
        "expected_comparison_flat_files_stylish.txt",
    ),
    (
        (PATH_NESTED_JSON_FILE1, PATH_NESTED_JSON_FILE2),
        "expected_comparison_nested_files_stylish.txt",
    ),
    (
        (PATH_NESTED_YAML_FILE1, PATH_NESTED_YAML_FILE2),
        "expected_comparison_nested_files_stylish.txt",
    ),
]

COMPARISON_PARAMETRS_WITH_FORMAT = [
    (
        (PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2, "stylish"),
        "expected_comparison_flat_files_stylish.txt",
    ),
    (
        (PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2, "plain"),
        "expected_comparison_flat_files_plain.txt",
    ),
    (
        (PATH_FLAT_YAML_FILE1, PATH_FLAT_YAML_FILE2, "plain"),
        "expected_comparison_flat_files_plain.txt",
    ),
    (
        (PATH_NESTED_JSON_FILE1, PATH_NESTED_JSON_FILE2, "plain"),
        "expected_comparison_nested_files_plain.txt",
    ),
    (
        (PATH_NESTED_YAML_FILE1, PATH_NESTED_YAML_FILE2, "plain"),
        "expected_comparison_nested_files_plain.txt",
    ),
    (
        (PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2, "json"),
        "expected_comparison_flat_files_json.txt",
    ),
    (
        (PATH_NESTED_JSON_FILE1, PATH_NESTED_JSON_FILE2, "json"),
        "expected_comparison_nested_files_json.txt",
    ),
]

CHECK_VALID_JSON_PARAMETRS = [
    (PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2, "json"),
    (PATH_NESTED_JSON_FILE1, PATH_NESTED_JSON_FILE2, "json"),
]


@pytest.mark.parametrize("parametrs", DEFAULT_COMPARISON_PARAMETRS)
def test_default_comparison_files(parametrs):
    expected = open(os.path.join(TEST_DATA_DIR, parametrs[1])).read()
    result = generate_diff(*parametrs[0])
    assert result == expected


@pytest.mark.parametrize("parametrs", COMPARISON_PARAMETRS_WITH_FORMAT)
def test_comparison_files_with_format(parametrs):
    expected = open(os.path.join(TEST_DATA_DIR, parametrs[1])).read()
    result = generate_diff(*parametrs[0])
    assert result == expected


@pytest.mark.parametrize("parametrs", CHECK_VALID_JSON_PARAMETRS)
def test_valid_json(parametrs):
    json.loads(
        generate_diff(PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2, "json")
    )
