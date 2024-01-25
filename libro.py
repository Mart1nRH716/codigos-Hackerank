def pageCount(n, p):
    # Write your code here
    counter_r = 0
    counter_l = 0
    
    for i in range(1, n+1, 2):
        if p == 1:
            break
        if p <= i:
            break
        counter_r += 1
        
    
    for j in range(n-1, -1, -2):
        if p == n:
            break
        if p >= j:
            break
        counter_l += 1

    if counter_r < counter_l:
        return counter_r
    else:
        return counter_l