#!/usr/bin/env python3

# Sample Input:
# this is an awesome text
# Sample Output:
# awesome

txt = input()
# txt = 'this is an awesome text'
txt = txt.split()

print(max(txt, key=len))
