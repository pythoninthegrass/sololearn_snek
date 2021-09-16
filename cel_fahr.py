celsius = int(input())

def conv(c):
    #your code goes here
    val = 9/5 * celsius + 32
    return val

fahrenheit = conv(celsius)
print(fahrenheit)
