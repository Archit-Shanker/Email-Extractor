#E-MAIL EXTRACTOR!!!!!
import re
stringg = input("Enter a string with an email address:")
pattern = r"([\w\.-]+)@([\w\-.]+)([\w\.-]+)"
match = re.search(pattern,stringg)
if match:
    print(match.group())
else:
    print("Your string does not contain an email address")