def waste(n):
    i = 1
    j = 1
    for i in range(n):
        for j in range(i):
            print(str(i) + ' ' + str(j) + ' ' + str(n))
    if(n > 0):
        for i in range(4):
            waste(n/2)

if __name__=="__main__":
    waste(10)
