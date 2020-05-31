string = input()
for i in range(len(string)-1):
    if string[i] == string[i+1] and string[i].isalnum():
        print(string[i])
        found = True
        break
    found = False
if not found:
    print(-1)
