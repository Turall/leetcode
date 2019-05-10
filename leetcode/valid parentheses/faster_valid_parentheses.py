def check(s):
    if not s:
        return True
    temp = []
    breckets = {"(": ")", "{": "}", "[": "]"}
    for parenthese in s:
        if parenthese in breckets:
            temp.append(parenthese)
        elif len(temp) == 0 or breckets[temp.pop()] != parenthese:
            return False
    return len(temp) == 0


print(check("()]"))
