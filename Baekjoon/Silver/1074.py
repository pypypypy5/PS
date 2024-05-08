import sys
input = sys.stdin.readline

N, r, c = map(int, input().split(' '))
width = 2**N

sum = 0
def whatitin(wid,y,x):   #y row x column
    global sum
    if wid > 2:
        n_wid = wid // 2
        if n_wid <= x:
            if n_wid <= y:
                sum += (n_wid**2)*3
                whatitin(n_wid,y-n_wid,x-n_wid)
            else:
                sum += (n_wid**2)
                whatitin(n_wid,y,x-n_wid)
        else:
            if n_wid <= y:
                sum += (n_wid**2)*2
                whatitin(n_wid,y-n_wid,x)
            else:
                whatitin(n_wid,y,x)
    else:
        if x == 0 and y == 0:
            sum += 0
        elif x == 1 and y == 0:
            sum += 1
        elif x == 0 and y == 1:
            sum += 2
        elif x == 1 and y == 1:
            sum += 3

whatitin(width,r,c)
print(sum)
