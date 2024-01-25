def is_one_away(str1, str2):
    if str1 == str2:
        return True
    counter = 0
    p = 0
    q = 0
    # bandera = True
    if abs(len(str1) - len(str2)) <= 1:
        while ( p < len(str1) and q < len(str2)):
            if str1[p] != str2[q]:
                counter += 1
                if len(str1) < len(str2):
                    q += 1
                elif len(str1) > len(str2):
                    p += 1
                else:
                    p += 1
                    q += 1  
            else:
                p += 1
                q += 1
    if p == q:
        counter += abs(len(str1) - len(str2))           
                    

    #print(counter)
    if counter > 1:
        return False
    else: return True

print(is_one_away("abcde", "abcd"))  # should return True
print(is_one_away("abde", "abcde"))  # should return True
print(is_one_away("a", "a"))  # should return True
print(is_one_away("abcdef", "abqdef"))  # should return True
print(is_one_away("abcdef", "abccef"))  # should return True
print(is_one_away("abcdef", "abcde"))  # should return True
print(is_one_away("aaa", "abc"))  # should return False
print(is_one_away("abcde", "abc"))  # should return False
print(is_one_away("abc", "abcde"))  # should return False
print(is_one_away("abc", "bcc"))  # should return False"
print(is_one_away("abcd", "abcedf"))  # should return False"