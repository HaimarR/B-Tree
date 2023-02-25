def curate(a_func : str):
    my_func = a_func.strip()
    tokens = my_func.split(" ")

    incogs, powers, signs, x_indexes = take_powers(tokens)
    return tokens, incogs, powers, signs, x_indexes

def take_powers(curated_func : list):
    incogs = []
    powers = dict()
    signs = []
    x_indexes = []
    for token in curated_func:
        if "x" in token:
            x_indexes.append(token.index("x"))
            incogs.append(token)
            if "**" in token:
                power = token[token.index("*") + 2]
                # print("Found power", power, "in token", token)
                powers[token] = power

        if token == "+" or token == "-" or token == "*" or token == "/":
            signs.append(token)

    return incogs, powers, signs, x_indexes

def main():
    print(curate("2x**2 + 3x**1 - 1"))

if __name__ == "__main__":
    main()