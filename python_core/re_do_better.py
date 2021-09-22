import re

quote = "Always do your best. Your best is going to change from moment to moment; it will be different when you are healthy as opposed to sick. Under any circumstance, simply do your best, and you will avoid self-judgment, self-abuse and regret"

word = input()
# flags = re.IGNORECASE
# result = re.findall(word, quote, flags)
result = re.findall(word, quote)
print(len(result))
