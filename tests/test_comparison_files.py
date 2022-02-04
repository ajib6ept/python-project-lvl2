from fixtures.flat_json_files_comparison_result import result as flat_result
from fixtures.nested_files_comparison_result import result as nested_result
from fixtures.flat_format_comparison_result import (
    flat_files_result,
    nested_files_result,
)

from gendiff.cli import generate_diff
from gendiff import cli

from gendiff.formatter.flat import flat_stylish

import sys


PATH_FLAT_JSON_FILE1 = "./tests/fixtures/flat_file1.json"
PATH_FLAT_JSON_FILE2 = "./tests/fixtures/flat_file2.json"

PATH_FLAT_YAML_FILE1 = "./tests/fixtures/flat_file1.yml"
PATH_FLAT_YAML_FILE2 = "./tests/fixtures/flat_file2.yml"

PATH_NESTED_JSON_FILE1 = "./tests/fixtures/nested_file1.json"
PATH_NESTED_JSON_FILE2 = "./tests/fixtures/nested_file2.json"

PATH_NESTED_YAML_FILE1 = "./tests/fixtures/nested_file1.yml"
PATH_NESTED_YAML_FILE2 = "./tests/fixtures/nested_file2.yml"


def test_comparion_flat_json_files():
    assert (
        generate_diff(PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2) == flat_result
    )


def test_comparion_flat_yaml_files():
    assert (
        generate_diff(PATH_FLAT_YAML_FILE1, PATH_FLAT_YAML_FILE2) == flat_result
    )


def test_comparion_nested_json_files():
    assert (
        generate_diff(PATH_NESTED_JSON_FILE1, PATH_NESTED_JSON_FILE2)
        == nested_result
    )


def test_comparion_nested_yaml_files():
    assert (
        generate_diff(PATH_NESTED_YAML_FILE1, PATH_NESTED_YAML_FILE2)
        == nested_result
    )


def test_comparion_flat_json_files():
    assert (
        generate_diff(PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2, flat_stylish)
        == flat_files_result
    )


def test_comparion_nested_json_files():
    assert (
        generate_diff(
            PATH_NESTED_JSON_FILE1, PATH_NESTED_JSON_FILE2, flat_stylish
        )
        == nested_files_result
    )
