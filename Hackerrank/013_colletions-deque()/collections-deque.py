from collections import deque
d = deque()
i = 0

for _ in range(int(input())):
    command = input()
    if command[0].isdigit():
        continue
        i+=1
    elif command == None:
        break
        i+=1
    elif command[-1].isdigit():
        command = command[0:-2] + "(" + command[-1] + ")"
    else:
        command = command + "()"
    eval("d." + command)
    i+=1

result_string = ""
for a in d: