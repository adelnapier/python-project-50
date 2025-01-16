import json

import yaml


def read_and_parse(file_path):
    if file_path.endswith(('.yml', '.yaml')):
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    elif file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            return json.load(file)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def main():
    file1 = 'file1.json'  # Или file1.yaml
    file2 = 'file2.json'  # Или file2.yaml

    data1 = read_and_parse(file1)
    data2 = read_and_parse(file2)

    print("Содержимое первого файла:")
    print(data1)
    print("\nСодержимое второго файла:")
    print(data2)


if __name__ == '__main__':
    main()
