import sys
input = sys.stdin.readline

num = int(input())
for i in range(num):
    got = input().strip()
    num_left = 0
    num_right = 0
    is_VPS = True

    if got[0] == ')' or got[-1] == '(':
        is_VPS = False
    
    else:
        for j in range(len(got)):
            if got[j] == '(':
                num_left += 1
            else:
                num_right += 1
            
            if num_left < num_right:
                is_VPS = False
                break

            if j == len(got)-1 and num_left != num_right:
                is_VPS = False
                break
    
    #for k in range(len(got)):
    #    print(got[k])
    if is_VPS:
        print('YES')
    else:
        print('NO')
