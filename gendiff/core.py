from gendiff.scripts.file_parser import read_and_parse


def generate_diff(file_path1, file_path2):
    data1 = read_and_parse(file_path1)
    data2 = read_and_parse(file_path2)

    keys = sorted(set(data1.keys()).union(data2.keys()))
    diff = []

    for key in keys:
        if key not in data2:
            diff.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            diff.append(f"  + {key}: {data2[key]}")
        elif data1[key] != data2[key]:
            diff.append(f"  - {key}: {data1[key]}")
            diff.append(f"  + {key}: {data2[key]}")
        else:
            diff.append(f"    {key}: {data1[key]}")

    return "{\n" + "\n".join(diff) + "\n}"
