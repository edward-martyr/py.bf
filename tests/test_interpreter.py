from io import StringIO
from pathlib import Path
from subprocess import check_output

from pybf.interpreter import Interpreter

from .utils import BaseTestCase


class TestInterpreter(BaseTestCase):
    def test_hello_world(self) -> None:
        string_io = StringIO()
        code = Path("tests/hello_world.bf").read_text()
        interpreter = Interpreter(code, output=string_io)
        interpreter.run()
        self.assertEqual(string_io.getvalue(), "Hello World!\n")

    def test_bash_hello_world(self) -> None:
        self.assertEqual(
            check_output(
                "python -m pybf hello_world.bf".split(),
                cwd="tests",
            )
            .decode()
            .strip(),
            "Hello World!",
        )
