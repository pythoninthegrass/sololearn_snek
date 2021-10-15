"""
Module 2 Quiz: Filter even numbers
"""
nums = ['1', '2', '8', '3', '7']
res = list(filter(lambda x: int(x) % 2 == 0, nums))
print(res)


"""
Code Project: Reverse a string and print on a new line
"""
def spell(txt):
    return txt[::-1]

txt = input()

print('\n'.join(map(str, spell(txt))))
