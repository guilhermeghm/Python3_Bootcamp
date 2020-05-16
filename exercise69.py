def interleave(str1, str2):
    return "".join("".join(i) for i in (zip(str1,str2)))

print(interleave("hi", "no"))
