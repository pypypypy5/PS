def is_valid_team_name(name):
    up = 0
    low = 0
    for i in name:
        if i.isupper():
            up += 1
        elif i.islower():
            low += 1
    
    if up > low:
        return False

    if len(name) > 10:
        return False

    num = False
    for i in name:
        if not i.isdigit():
            num = True
            break

    return num

n = int(input())
team_names = [input() for i in range(n)]

for i in team_names:
  if is_valid_team_name(i):
    print(i)
    break
