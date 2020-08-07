def swap_case(s):
    newstring = ""
    for char in s:
        if char.isupper():
            newstring += char.lower()
        else:
            newstring += char.upper()
    return(newstring)

if __name__ == '__main__':