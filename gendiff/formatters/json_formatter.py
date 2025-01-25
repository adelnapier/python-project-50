import json


def format_diff(diff):
    """
    Форматирует diff в JSON-формате.
    """
    return json.dumps(diff, indent=4)
