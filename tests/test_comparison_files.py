import json

from gendiff.cli import generate_diff
from tests.fixtures.plain_format_comparison_result import (
    flat_files_result as plain_flat_result,
)
from tests.fixtures.plain_format_comparison_result import (
    nested_files_result as plain_nested_result,
)
from tests.fixtures.stylish_format_comparison_result import (
    flat_files_result as stylish_flat_result,
)
from tests.fixtures.stylish_format_comparison_result import (
    nested_files_result as stylish_nested_result,
)

PATH_FLAT_JSON_FILE1 = "./tests/fixtures/flat_file1.json"
PATH_FLAT_JSON_FILE2 = "./tests/fixtures/flat_file2.json"

PATH_FLAT_YAML_FILE1 = "./tests/fixtures/flat_file1.yml"
PATH_FLAT_YAML_FILE2 = "./tests/fixtures/flat_file2.yml"

PATH_NESTED_JSON_FILE1 = "./tests/fixtures/nested_file1.json"
PATH_NESTED_JSON_FILE2 = "./tests/fixtures/nested_file2.json"

PATH_NESTED_YAML_FILE1 = "./tests/fixtures/nested_file1.yml"
PATH_NESTED_YAML_FILE2 = "./tests/fixtures/nested_file2.yml"


def test_default_comparison_flat_json_files():
    assert (
        generate_diff(PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2)
        == stylish_flat_result
    )


def test_default_comparison_flat_yaml_files():
    assert (
        generate_diff(PATH_FLAT_YAML_FILE1, PATH_FLAT_YAML_FILE2)
        == stylish_flat_result
    )


def test_default_comparion_nested_json_files():
    assert (
        generate_diff(PATH_NESTED_JSON_FILE1, PATH_NESTED_JSON_FILE2)
        == stylish_nested_result
    )


def test_default_comparion_nested_yaml_files():
    assert (
        generate_diff(PATH_NESTED_YAML_FILE1, PATH_NESTED_YAML_FILE2)
        == stylish_nested_result
    )


def test_stylish_comparison_flat_json_files():
    assert (
        generate_diff(PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2, "stylish")
        == stylish_flat_result
    )


def test_plain_comparison_flat_json_files():
    assert (
        generate_diff(PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2, "plain")
        == plain_flat_result
    )


def test_plain_comparison_flat_yml_files():
    assert (
        generate_diff(PATH_FLAT_YAML_FILE1, PATH_FLAT_YAML_FILE2, "plain")
        == plain_flat_result
    )


def test_plain_comparison_nested_json_files():
    assert (
        generate_diff(PATH_NESTED_JSON_FILE1, PATH_NESTED_JSON_FILE2, "plain")
        == plain_nested_result
    )


def test_plain_comparison_nested_yml_files():
    assert (
        generate_diff(PATH_NESTED_YAML_FILE1, PATH_NESTED_YAML_FILE2, "plain")
        == plain_nested_result
    )


def test_comparion_flat_json_files_stylish_json():
    json.loads(
        generate_diff(PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2, "json")
    )


def test_comparion_nested_json_files_stylish_json():
    json.loads(
        generate_diff(PATH_NESTED_JSON_FILE1, PATH_NESTED_JSON_FILE2, "json")
    )
