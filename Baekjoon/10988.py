inp_str = list(input())

length = len(inp_str)

if length % 2 == 0:
    half = length // 2
else:
    half = (length-1) // 2

palindrome = True

for i in range(half):
    if inp_str[i] != inp_str[-(i+1)]:
        palindrome = False
        break

if palindrome == True:
    print(1)
else:
    print(0)