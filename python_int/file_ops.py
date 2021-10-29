import os
from pathlib import Path

home = os.path.expandvars("$HOME")
cwd = os.path.dirname(os.path.abspath("__file__"))
fn = Path(cwd) / "python_core/books.txt"            # .. == Path(cwd).parent / "books.txt"

with open(fn, "r") as file:
    # print(file.read())
    for count, line in enumerate(file):
        line_no = count + 1
        print(f"Line {line_no}:", str(len(line.split())), "words")
    # print('Total Lines', count + 1)
