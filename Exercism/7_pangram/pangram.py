def is_pangram(sentence):
    counter = 0
    alphabeth = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabeth:
        if char in sentence.lower():
            counter+=1
    return counter == 26
