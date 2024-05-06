import sys
input = sys.stdin.readline

num = int(input())
seq = []
num_dict = dict()
for i in range(num):
    got = int(input())
    seq.append(got)
    if got not in num_dict:
        num_dict[got] = 1
    else:
        num_dict[got] += 1

def second_max_key(d):
  maxi = max(d.values())
  max_keys = [key for key, value in d.items() if value == maxi]
  max_keys.sort()
  if len(max_keys) < 2:
    return max_keys[0]
  return max_keys[1]


seq.sort()
print(f'{round(sum(seq)/num)}')
print(seq[num//2])
print(second_max_key(num_dict))
print(seq[num-1]-seq[0])
