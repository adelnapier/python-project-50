def format_value(value):
    """Форматирование значений для plain вывода."""
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    return value


def format_diff(diff, parent=''):
    """Форматирование diff в стиле plain."""
    lines = []

    for node in diff:
        key = node['key']
        full_path = f"{parent}.{key}" if parent else key

        if node['type'] == 'added':
            value = format_value(node['value'])
            lines.append(
                f"Property '{full_path}' was added with value: {value}"
            )
        elif node['type'] == 'removed':
            lines.append(f"Property '{full_path}' was removed")
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(
                f"Property '{full_path}' was updated. "
                f"From {old_value} to {new_value}"
            )
        elif node['type'] == 'nested':
            lines.append(format_diff(node['children'], full_path))

    return '\n'.join(lines)
