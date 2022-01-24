from fixtures.flat_json_files_comparison_result import result

from gendiff.cli import generate_diff


PATH_FLAT_JSON_FILE1 = "./tests/fixtures/flat_file1.json"
PATH_FLAT_JSON_FILE2 = "./tests/fixtures/flat_file2.json"


def test_comparion_flat_json_files():
    assert generate_diff(PATH_FLAT_JSON_FILE1, PATH_FLAT_JSON_FILE2) == result