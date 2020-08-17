high = 11
long = 33
longhalf = long//2
lines = 1
for i in range(high//2):
    if i < high//2:
        print("-"*(longhalf-1-(3*i)) + ".|."*(lines) + "-"*(longhalf-1-(3*i)))
    lines+=2
print("-"*(longhalf-3) + "WELCOME" + "-"*(longhalf-3))
lines += -2
for i in range(high//2):
    print("-"*(3+3*i) + ".|."*(lines) + "-"*(3+3*i))
    lines += -2
