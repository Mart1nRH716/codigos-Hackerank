def divisibleSumPairs(n, k, ar):
    # Write your code here
    ini = 0
    fin = 0
    count = 0
    
    for i in range(n):
        ini = i
        fin = ini + 1
        for j in range(n):
            if ini >= len(ar) or fin >= len(ar):
                break
            if (ar[ini] + ar[fin]) % k == 0:
                count += 1
            fin += 1
        
    
    return count

ar = [1, 3, 2, 6, 1, 2]
n = 6
k = 3
print(divisibleSumPairs(n, k, ar))