def translate(s):
    t = ""
    for i in s:
        if i in "AEIOUaeiou":
            t += "g"
        else:
            t += i
    return t

print(translate("dogs are cool"))