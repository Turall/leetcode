def lengthOfLastWord(s):
    s = s.split()
    try:
        return len(s[-1])
    except:
        return 0

