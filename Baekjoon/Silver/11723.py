import sys
input = sys.stdin.readline


M = int(input())
s = set()

for i in range(M):
    got = input()
    try:
        command, att = got.split(' ')
        att = float(att)
    except:
        command = got.strip()

    if command == 'add':
        try:
            s.add(att)
        except:
            pass

    elif command == 'remove':
        try:
            s.remove(att)
        except:
            pass
        
    elif command == 'check':
        if att in s:
            print(1)

        else:
            print(0)


    elif command == 'toggle':
        if att in s:
            s.remove(att)
        else:
            s.add(att)
        
    elif command == 'all':
        s = set([i for i in range(1,21)])

    elif command == 'empty':
        s = set()
