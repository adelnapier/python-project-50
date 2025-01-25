from gendiff.diff_builder import build_diff
from gendiff.formatters.plain import format_diff as plain_format
from gendiff.formatters.stylish import format_diff as stylish_format
from gendiff.scripts.file_parser import read_and_parse

FORMATTERS = {
    'stylish': stylish_format,
    'plain': plain_format,
}


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Генерация diff с выбором формата."""
    data1 = read_and_parse(file_path1)
    data2 = read_and_parse(file_path2)
    diff = build_diff(data1, data2)

    format_func = FORMATTERS.get(format_name)
    if not format_func:
        raise ValueError(f"Unknown format: {format_name}")
    return format_func(diff)
