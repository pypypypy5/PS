import sys
input = sys.stdin.readline

num_n = int(input().rstrip())
original = list(map(int, input().split()))


std_set = set(original)
std_li = list(std_set)
std_li.sort()


dict = {}
for i in range(len(std_li)):
    dict[std_li[i]] = i


for i in range(num_n):
    if i != num_n-1:
        print(dict[original[i]], end = ' ')
    else:
        print(dict[original[i]])