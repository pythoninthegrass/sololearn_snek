import re
# text = input()
text = r"#Coding is #awesome !!"
pattern = r"#\w+"
print("\n".join((re.findall(pattern, text))))
