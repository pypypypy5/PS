import sys
input = sys.stdin.readline

num = int(input())
li = [1,2,3]
log = []

def moveto(fr,to,stack):
    if stack != 1:
        li_togo = [1,2,3]
        li_togo.remove(fr)
        li_togo.remove(to)
        willgo = li_togo[0]


        
        moveto(fr,willgo,stack-1)
        log.append(f'{fr} {to}')
        moveto(willgo,to,stack-1)
    else:
        log.append(f'{fr} {to}')

moveto(1,3,num)
print(len(log))
for i in log:
    print(i)

