from pathlib import Path
from sys import stderr, stdin

from .compiler import Compiler
from .interpreter import Interpreter


def main():
    import argparse

    arg_parser = argparse.ArgumentParser(
        prog="pybf", description="brainfuck interpreter"
    )
    arg_parser.add_argument(
        "-p", "--python", dest="use_python", action="store_true", default=True
    )
    arg_parser.add_argument("-c", "--c", dest="use_python", action="store_false")
    arg_parser.add_argument(
        "--compile", dest="if_compile", action="store_false", default=False
    )
    arg_parser.add_argument(
        "-r", "--run", dest="if_run", action="store_true", default=False
    )
    arg_parser.add_argument("filename", nargs="?")
    args = arg_parser.parse_args()

    if args.filename:
        code = Path(args.filename).read_text()
    else:
        code = stdin.read()
        args.filename = "<stdin>"
    if args.use_python:
        interpreter = Interpreter(code, filename=args.filename)
        interpreter.run()
    else:
        if args.if_run:
            args.if_compile = True

        compiler = Compiler(code, filename=args.filename)
        compiler.transpile()

        if args.if_compile:
            compiler.compile()
        if args.if_run:
            compiler.run()


if __name__ == "__main__":
    main()
