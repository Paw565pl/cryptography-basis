from argparse import ArgumentParser
from sys import argv

import affine
import cesar


def main():
    parser = ArgumentParser(description="cesar and affine cypher implementation")

    cypher_group = parser.add_mutually_exclusive_group(required=True)
    cypher_group.add_argument("-c", help="cesar cipher", action="store_true")
    cypher_group.add_argument("-a", help="affine cipher", action="store_true")

    operation_group = parser.add_mutually_exclusive_group(required=True)
    operation_group.add_argument("-e", help="encrypt", action="store_true")
    operation_group.add_argument("-d", help="decrypt", action="store_true")
    operation_group.add_argument("-j", help="find key", action="store_true")
    operation_group.add_argument("-k", help="break code", action="store_true")

    parser.parse_args()

    cypher_argument = argv[1]
    operation_argument = argv[2]

    args_to_function = {
        "-c": {
            "-e": cesar.encrypt,
            "-d": cesar.decrypt,
            "-j": cesar.find_key,
            "-k": cesar.break_code,
        },
        "-a": {
            "-e": affine.encrypt,
            "-d": affine.decrypt,
            "-j": affine.find_key,
            "-k": affine.break_code,
        },
    }

    args_to_function[cypher_argument][operation_argument]()
    print("done!")


if __name__ == "__main__":
    main()
