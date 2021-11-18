from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
cwd = base_dir / 'python_core'
fn = f"{cwd}/books.txt"

"""
Read the file and split the lines into a list.
Flatten the list except for the empty strings.
Split each string into a list of words.
Create a list of the first letter of each word.
Join the list into a string with no spaces.
Print the string on a new line.
"""
with open(fn, "r") as file:
    titles = file.read().split(sep="\n")
    titles[:] = [x for x in titles if x != '']

    res = []
    for i in titles:
        split_title = i.split(" ")
        acro = [x[0][0] for x in split_title]
        res.append("".join(acro))

    for i in res:
        print(i)
