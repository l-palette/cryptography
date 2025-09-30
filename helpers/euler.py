from collections import defaultdict
from helpers.log import print_powers, print_factorisation


def factors(n: int) -> dict:
    init_n = n
    powers = defaultdict(int)
    i = 2
    while n != 1:
        remainder = n % i
        if remainder == 0:
            while n % i == 0:
                print_factorisation(n, i, tabs=0)
                n //= i
                powers[i] += 1
        i += 1
    print(1)
    print_powers(init_n, powers)
    return powers


def phi(n: int) -> int:
    """
    phi(p^a) = p^a - p^{a-1}
    """
    powers = factors(n)
    phi = 1
    phis = []
    for base, exp in powers.items():
        if exp == 1:
            cur_phi = base - 1
            print(f"phi({base}) = {base} - 1 = {cur_phi}")
        else:
            cur_phi = pow(base, exp) - pow(base, exp - 1)
            print(
                f"phi({base}^{exp}) = {base}^{exp} - {base}^{exp - 1} = {pow(base, exp)} - {pow(base, exp-1)} = {cur_phi}"
            )

        phi *= cur_phi
        phis.append(str(cur_phi))
    if len(phis) > 1:
        print(f'phi = {" * ".join(phis)} = {phi}')

    return phi
