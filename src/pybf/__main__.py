from pathlib import Path
from sys import stderr, stdin

from .interpreter import Interpreter


def main():
    import argparse

    arg_parser = argparse.ArgumentParser(
        prog="pybf", description="brainfuck interpreter"
    )
    arg_parser.add_argument("-p", dest="use_python", action="store_true", default=True)
    arg_parser.add_argument("-c", dest="use_python", action="store_false")
    arg_parser.add_argument(
        "--no-run", dest="if_run", action="store_false", default=True
    )
    arg_parser.add_argument("filename", nargs="?")
    args = arg_parser.parse_args()

    if args.use_python:
        if not args.if_run:
            print("Must directly execute file in Python mode!", file=stderr)
            return
        if args.filename:
            code = Path(args.filename).read_text()
        else:
            code = stdin.read()
            args.filename = "<stdin>"
        interpreter = Interpreter(code, filename=args.filename)
        interpreter.run()


if __name__ == "__main__":
    main()
