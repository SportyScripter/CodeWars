def printer_error(s):
    alphabet = "abcdefghijklm"
    count = 0
    for i in s:
        if i not in alphabet:
            count += 1
    return str(count) + "/" + str(len(s))

