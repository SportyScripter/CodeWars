# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.
def accum(s):
    index = 1
    new_string = ""
    for i in s:
        if isinstance(i,str):
            new_string += i.upper()
            if index > 1:
                for n in range(index-1):
                    new_string+= i.lower()
            if index < len(s):
                new_string+= "-"
        index += 1
    return new_string

                
        
print(accum("abcd"))
print(accum("RqaEzty"))
print(accum("cwAt"))
        
        
        



