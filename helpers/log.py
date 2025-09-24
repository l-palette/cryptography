from tabulate import tabulate

def pretty_print(text: str, grid="heavy_grid"):
    print(tabulate([[text]], tablefmt=grid))

def print_division(a: int, b: int, quotient: int, remainder: int, tabs=1):
    tab = '\t' * tabs
    print(f'{tab}{a} |_{b}')
    temp = b * quotient
    print(f'{tab}{temp}  {quotient}')
    print(f'{tab}__')
    print(f'{tab}{remainder}')
    print()

def print_factorisation(a: int, b: int, tabs=1):
    tab = '\t' * tabs
    print(f'{tab}{a} | {b}')


def print_powers(number, powers: dict):
    factors = []
    for base, exp in powers.items():
        if exp != 1:
            factors.append(f"{base}^{exp}")
        else:
            factors.append(f"{base}")
    if len(factors) > 1:
        factors_str = " * ".join(factors)
        pretty_print(f"{number} = {factors_str}", 'grid')
    else:
        pretty_print(f"{number} - простое число", 'grid')
