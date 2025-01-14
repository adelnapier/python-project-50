import argparse

from gendiff.core import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", type=str, help="Path to the first file")
    parser.add_argument("second_file", type=str, help="Path to the second file")
    parser.add_argument("-f", "--format", type=str, help="Set format of output")

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
