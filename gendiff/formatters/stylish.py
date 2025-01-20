def format_diff(diff, depth=1):
    lines = []
    indent = '  ' * depth
    for item in diff:
        key = item['key']
        item_type = item['type']
        if item_type == 'nested':
            children = format_diff(item['children'], depth + 1)
            lines.append(f"{indent}  {key}: {{\n{children}\n{indent}  }}")
        elif item_type == 'added':
            lines.append(f"{indent}+ {key}: {item['value']}")
        elif item_type == 'removed':
            lines.append(f"{indent}- {key}: {item['value']}")
        elif item_type == 'changed':
            lines.append(f"{indent}- {key}: {item['old_value']}")
            lines.append(f"{indent}+ {key}: {item['new_value']}")
        elif item_type == 'unchanged':
            lines.append(f"{indent}  {key}: {item['value']}")
    return '\n'.join(lines)
