def staircase(n):
    # Write your code here
    s = 1 # cantidad de simbolos
    e = n-1  #cantidad de espacios
    c = '#'
    c2 = ' '
   
    for i in range(n):
        j = 0 
        t = 0 
        while j < e:
            print (c2, end="")
            j+=1
        while( t < s):
            print (c,end="")
            t +=1
        print("")
        s +=1
        e -= 1

            
            

if __name__ == '__main__':
    n = 6

    staircase(n)