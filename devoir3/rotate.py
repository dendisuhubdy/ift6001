stack = []
    
def push(i,j,d,M):
    for x in range(i,i+d):
        for y in range(j,j+d):
            stack.append(M[x][y])
                
def pull(i,j,d,M):
        
    for x in range(i,i+d):
        for y in range(j,j+d):
            M[x][y] = stack.pop()
                
def rotate(M):
    if (len(M)) == 2:
        
        push(0,0,2,M)
        pull(1,0,1,M)
        pull(0,0,1,M)
        pull(1,1,1,M)
        pull(0,1,1,M)
        return M
    else:
        n = len(M)/2
        push(n,0,n,M)
        M[n:,:n] = rotate(M[n:,n:])
        M[n:,n:] = rotate(M[:n,n:])
        M[:n,n:] = rotate(M[:n,:n])
        count =1
        for i in range(0,n):
            for j in range(0,n):
                count +=1
                pull(n-i-1,n-j-1,1,M)
        print count
        M[:n,:n] = rotate(M[:n,:n])
        return M

blocks = {(8,3,16),(2,3,6),(8,5,11),(25,2,125),(14,3,18),(7,6,10),(14,1,30)}
def panoramix(E):
    x = sorted(E)
    print x
    pano = [[0,0,0]]
    list_blocks = [0]*len(E)
    for i,block in enumerate(x):
        list_blocks[i] = list(block)
    pano = [list_blocks[0]]
    pano_count = 0
    for i in range(1,len(list_blocks)):
        if list_blocks[i][2]<=pano[pano_count][2]:
            print list_blocks[i]
            print pano[pano_count]
            continue
        pano.append([0,0,0])
        if pano[pano_count][1] != list_blocks[i][1]:
            pano[pano_count][2] = list_blocks[i][0]
            pano_count +=1
            pano[pano_count][0] = list_blocks[i][0]
            pano[pano_count][1] = list_blocks[i][1]
            pano[pano_count][2] = list_blocks[i][2]
        else:
            pano[pano_count][2] = list_blocks[i][2]
    return pano
