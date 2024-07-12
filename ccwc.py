import os
from argparse import ArgumentParser


def main():
    args = parser.parse_args()
    if args.b:
        print(bytes_counter(args))


parser = ArgumentParser(
    prog="Code Challenge Word Counter",
    description="Counts bytes, lines, words, characters in a file",
    epilog="help placeholder"
    )
parser.add_argument('filename')
parser.add_argument("-b", action="store_true", help="Counts bytes in a file")


def bytes_counter(args):
    result = os.path.getsize(args.filename)
    return result







if __name__ == "__main__":
    main()