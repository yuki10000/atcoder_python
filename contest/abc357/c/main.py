N = int(input())


def print_sharp(N):
    for i in range(N):
        print("###", end="")


def print_sharp_dot(N):
    for i in range(N):
        print("#.#", end="")


def print_dot(N):
    for i in range(N):
        print("...", end="")


def print_sharp_with_center(N):
    for i in range(N-1):
        if i >= 3 ** (N - 2) and i < 3 ** (N - 2) * 2:
            print_dot(3 ** (N - 2))
        else:
            print_sharp(3 ** (N - 2))


def print_sharp_dot_with_center(N):
    for i in range(3 ** (N-1)):
        if i >= 3 ** (N - 2) and i < 3 ** (N - 2) * 2:
            print_dot(3 ** (N - 2))
        else:
            print_sharp_dot(3 ** (N - 2))


def print_center(i, N):
    if i % 3 == 1:
        print_sharp_dot_with_center(N)
        # print("\n")
    else:
        print_sharp_with_center(N)
        # print("\n")


def print_carpet(N):
    for i in range(3 ** N):
        if i >= 3 ** (N - 1) and i < 3 ** (N - 1) * 2:
            print_center(i, N)
            # print("\n")
        elif i % 3 == 1:
            print_sharp_dot(3 ** (N - 1))
            # print("\n")
        else:
            print_sharp(3 ** (N - 1))
            # print("\n")


if (N == 1):
    print("###")
    print("#.#")
    print("###")
else:
    print_carpet(N)
