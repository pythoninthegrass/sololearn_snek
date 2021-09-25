# list `[]` of tuples `()`
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

person = input()

# unpack list of tuples w/list comprehension
res = [(name, age) for name, age in contacts]

# flatten list of tuples as string for sanity check
# then loop through list of tuples and print tuple indices 0 and 1
if person not in str(res):
    print("Not found")
else:
    for name, age in res:
        if name == person:
            print(f"{name} is {age}")
