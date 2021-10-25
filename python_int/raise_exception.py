tweet = input()

try:
    if len(tweet) > 42:
        raise ValueError("Tweet is too long")
except:
    print("Error")
else:
    print("Posted")
