import math

def solve_cubic(A, B, C, D):
    # Normalize coefficients
    a = B / A
    b = C / A
    c = D / A

    # Depressed cubic: t^3 + p*t + q = 0
    p = b - a**2 / 3
    q = (2 * a**3) / 27 - (a * b) / 3 + c

    # Discriminant
    D_discriminant = (q / 2)**2 + (p / 3)**3

    roots = []

    if abs(D_discriminant) < 1e-12:
        D_discriminant = 0.0

    if D_discriminant > 0:
        # One real root
        sqrt_D = math.sqrt(D_discriminant)
        u_cubed = -q / 2 + sqrt_D
        v_cubed = -q / 2 - sqrt_D

        # Cube roots handling negative values
        u = math.copysign(abs(u_cubed) ** (1/3), u_cubed)
        v = math.copysign(abs(v_cubed) ** (1/3), v_cubed)

        t = u + v
        x = t - a / 3
        roots.append(x)
    elif D_discriminant == 0:
        # Triple or double root
        if q == 0:
            t = 0
            x = t - a / 3
            roots.append(x)
        else:
            u = (-q / 2) ** (1/3)
            t1 = 2 * u
            t2 = -u
            x1 = t1 - a / 3
            x2 = t2 - a / 3
            roots.extend([x1, x2])
    else:
        # Three real roots
        r = math.sqrt(- (p**3) / 27)
        phi = math.acos(-q / (2 * r))
        m = 2 * (-p / 3) ** 0.5

        t1 = m * math.cos(phi / 3)
        t2 = m * math.cos((phi + 2 * math.pi) / 3)
        t3 = m * math.cos((phi + 4 * math.pi) / 3)

        x1 = t1 - a / 3
        x2 = t2 - a / 3
        x3 = t3 - a / 3
        roots.extend([x1, x2, x3])

    # Remove duplicates within tolerance
    unique_roots = []
    for r in roots:
        if not any(abs(r - ur) < 1e-8 for ur in unique_roots):
            unique_roots.append(r)

    # Sort roots
    unique_roots.sort()

    return unique_roots

def main():
    N = int(input())
    for _ in range(N):
        coeffs = input().split()
        while len(coeffs) < 4:
            coeffs += input().split()
        A, B, C, D = map(float, coeffs)
        roots = solve_cubic(A, B, C, D)
        print(' '.join(f'{r:.4f}' for r in roots))

if __name__ == "__main__":
    main()
