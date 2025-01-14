def main()-> None:
    x:int = get_int("what's x: ")
    print(f"x is {x}")


def get_int(prompt:str)-> int:
    while True:
        try:
            x:int = int(input(prompt))
            return x
        except ValueError:
            print("X is not an integer.")
            pass


if __name__ == "__main__":
    main()