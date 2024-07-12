import os
from argparse import ArgumentParser


def main():
    args = parser.parse_args()
    if args.b:
        print(bytes_counter(args))
    elif args.l:
        print(lines_counter(args))
    else:
        parser.print_help()


parser = ArgumentParser(
    prog="Code Challenge Word Counter",
    description="Counts bytes, lines, words, characters in a file",
    epilog="help placeholder"
    )
parser.add_argument('filename')
parser.add_argument("-b", action="store_true", help="Counts bytes in a file")
parser.add_argument("-l", action="store_true", help="Counts lines in a file")


def bytes_counter(args):
    result = os.path.getsize(args.filename)
    return result

def lines_counter(args):
    result = 0
    with open(args.filename, 'r', encoding='UTF-8') as file:
        for _ in file.readlines():
            result += 1
    return result







if __name__ == "__main__":
    main()