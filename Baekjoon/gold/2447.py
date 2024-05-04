def fractal(n):
    if n == 1:
        return ['*']
    
    shape_bef = fractal(n//3)
    output_aft = []

    for i in shape_bef:
        output_aft.append(i*3)
    for i in shape_bef:
        output_aft.append(i + ' '*(n//3) + i)
    for i in shape_bef:
        output_aft.append(i*3)

    return output_aft

N = int(input())
got = fractal(N)
for i in got:
    print(i)
