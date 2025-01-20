from gendiff.formatters.stylish import format_diff
from gendiff.scripts.file_parser import read_and_parse


def build_diff(data1, data2):
    diff = []
    keys = sorted(set(data1.keys()).union(data2.keys()))

    for key in keys:
        if key not in data2:
            diff.append({
                'key': key,
                'type': 'removed',
                'value': data1[key],
            })
        elif key not in data1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': data2[key],
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff(data1[key], data2[key]),
            })
        elif data1[key] != data2[key]:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key],
            })
        else:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': data1[key],
            })
    return diff


def generate_diff(file_path1, file_path2):
    data1 = read_and_parse(file_path1)
    data2 = read_and_parse(file_path2)
    diff = build_diff(data1, data2)
    return format_diff(diff)
