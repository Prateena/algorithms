def KMP(text, pattern):

    if not pattern:
        return

    if not text or len(pattern) > len(text):
        print("Pattern Not Found")
        return
    
    chars = list(pattern)
    print(chars,34584305843)

    next = [0] * (len(pattern) + 1)

    for i in range(1, len(pattern)):
        j = next[i]

        if j > 0 and chars[j] is not chars[i]:

            j = next[j]

        if j > 0 and chars[j] == chars[i]:
            next[i + 1] = j + 1   

    i, j = 0, 0
    while i < len(text):
        if j < len(pattern) and text[i] == pattern[j]:
            j = j + 1
            if j == len(pattern):
                print("The pattern occurs with shift ", i - j + 1) 
        elif j > 0:
            j = next[j]
            i -= 1
        i += 1

if __name__ == '__main__':

    text = "ABCABAABCABACABC"
    pattern = "ABC"

    KMP(text, pattern)
    
