#!/usr/bin/env python3

# SOURCES
# https://www.programiz.com/python-programming/examples/fibonacci-recursion
# https://realpython.com/python-range/

def fibonacci(n):
	if n <= 1:
		return n
	else:
		return(fibonacci(n - 1) + fibonacci(n - 2))
		
def main():
	for i in range(0, num):
		print(fibonacci(i))
		
if __name__ == "__main__":
	#num = int(input("Enter an integer plz\n"))
	num = int(input())
	main()

