def main():
    x = input("What's x? ")
    print("x squared is", square(x))


def square(n):
    return n * n    # adding a bug intentionally


if __name__ == "__main__":
    main()