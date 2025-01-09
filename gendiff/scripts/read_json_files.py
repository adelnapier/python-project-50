import json

def read_and_parse(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    data1 = read_and_parse('file1.json')
    data2 = read_and_parse('file2.json')

    print("Содержимое file1.json:")
    print(data1)
    print("\nСодержимое file2.json:")
    print(data2)

if __name__ == '__main__':
    main()
