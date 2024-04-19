#!/usr/bin/env python3

from gendiff.gendiff import generate_diff
from gendiff.parser import parser


def main():
    args = parser()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
