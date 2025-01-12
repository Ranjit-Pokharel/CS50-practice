def main()-> None:
    x:int = int(input("What's X: ").strip())
    if is_even(num=x):
        print("Even.")
    else:
        print("Odd.")


def is_even(num:int)-> bool:
    return True if num % 2 == 0 else False


if __name__ == "__main__":
    main()