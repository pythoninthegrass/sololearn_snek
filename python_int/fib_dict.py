fib = {1: 1, 2: 1, 3: 2, 4: 3}

# get method looks for value (4), then supplies default if not found (0)
print(fib.get(4, 0) + fib.get(7, 5))
