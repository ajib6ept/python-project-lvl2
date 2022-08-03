from gendiff.formatter.default import stylish
from gendiff.formatter.plain import plain_stylish
from gendiff.formatter.jsonf import json_stylish

FORMATTERS = {
    "stylish": stylish,
    "plain": plain_stylish,
    "json": json_stylish,
}


def get_formatter(formatter_name):
    return FORMATTERS[formatter_name]
