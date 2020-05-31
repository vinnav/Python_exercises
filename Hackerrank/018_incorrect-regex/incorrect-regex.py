import re
for _ in range(int(input())):
    regex = input()
    try:
        re.compile(regex)
        print(True)
    except re.error:
        print(False)