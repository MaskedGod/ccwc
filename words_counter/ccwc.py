import sys
from argparse import ArgumentParser
from rich import print


def main():
    args = parser.parse_args()
    if args.filename:
        fname = args.filename
    else:
        fname = sys.stdin.readline().split('\n')[0]
    if args.b:
        print(bytes_counter(fname))
    elif args.l:
        print(lines_counter(fname))
    elif args.w:
        print(words_counter(fname))
    elif args.c:
        print(characters_counter(fname)) 
    else:
        print(lines_counter(fname), words_counter(fname), bytes_counter(fname), sep=" ",)


parser = ArgumentParser(
    prog="Code Challenge Word Counter",
    description="Counts bytes, lines, words, characters in a file",
    epilog="help placeholder"
    )

parser.add_argument('filename', nargs='?', default=None, help="The name of the file to process. If not provided, input is read from stdin.")
parser.add_argument("-b", action="store_true", help="Counts bytes in a file")
parser.add_argument("-l", action="store_true", help="Counts lines in a file")
parser.add_argument("-w", action="store_true", help="Counts words in a file")
parser.add_argument("-c", action="store_true", help="Counts characters in a file")


def bytes_counter(fname):
    result = 0
    with open(fname, 'rb') as file:
        result = len(file.read())
    return result

def lines_counter(fname):
    result = 0
    with open(fname, 'r', encoding='utf-8') as file:
        for _ in file.readlines():
            result += 1
    return result

def words_counter(fname):
    result = 0
    with open(fname, 'r', encoding='utf-8') as file:
        for row in file.readlines():
            words_amount = len(row.split())
            result += words_amount
    return result

def characters_counter(fname):
    result = 0
    with open(fname, 'r', encoding='utf-8') as file:
        for row in file.read():
            characters_amount = len(row)
            result += characters_amount
    return result







if __name__ == "__main__":
    main()