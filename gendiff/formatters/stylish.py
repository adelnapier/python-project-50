def to_string(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        # True -> 'true', False -> 'false'
        return str(value).lower()
    return str(value)

def format_diff(diff, depth=2):
    lines = []
    indent = '  ' * depth
    for item in diff:
        key = item['key']
        item_type = item['type']

        if item_type == 'nested':
            children = format_diff(item['children'], depth + 1)
            lines.append(f"{indent}  {key}: {{\n{children}\n{indent}  }}")

        elif item_type == 'added':
            lines.append(
                f"{indent}+ {key}: {to_string(item['value'])}"
            )

        elif item_type == 'removed':
            lines.append(
                f"{indent}- {key}: {to_string(item['value'])}"
            )

        elif item_type == 'changed':
            lines.append(
                f"{indent}- {key}: {to_string(item['old_value'])}"
            )
            lines.append(
                f"{indent}+ {key}: {to_string(item['new_value'])}"
            )

        elif item_type == 'unchanged':
            lines.append(
                f"{indent}  {key}: {to_string(item['value'])}"
            )

    return '\n'.join(lines)
