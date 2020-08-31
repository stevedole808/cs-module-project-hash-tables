# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
x = open('applications/crack_caesar/ciphertext.txt', "r")
cipher = x.read().lower()
x.close()

def count(s):
    d = {}
    for i in s:
        if i.isspace():
            continue
        if i not in d:
            d[i] = 0
        d[i] += 1
        
    return d

def sort_by_value(s):
    j = count(s)
    letters = list(j.items())
    letters.sort(key=lambda e: e[1], reverse=True)

    for i in letters:
        print(f"{i[0]}: appears {i[1]} times")

count(cipher)