def appendAndDelete(s, t, k):
    # Write your code here
    if s == t:
        return "Yes"
    movimientos = 0
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                movimientos = 2*(len(s) - i)
                break
    elif len(s) > len(t):
        for i in range(len(t)):
            if s[i] != t[i]:
                movimientos = (len(s) - i) + (len(s) - len(t))
                break
        movimientos += len(s) - len(t)
    elif len(s) < len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                movimientos = len(t) - i
                break
        movimientos += len(t) - len(s)
    
                
    if movimientos > k:
        return "No"
    else:
        return "Yes"
    
print(appendAndDelete("abcd", "abcdert", 10))