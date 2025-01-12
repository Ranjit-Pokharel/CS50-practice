class Statements:
    def __init__(
        self,
    ) -> None:
        pass

    def compare(self, x: int, y: int) -> int:
        if x < y:
            return -1
        elif x > y:
            return 1
        else:
            return 0

    def isequal(self, x: int, y: int) -> bool:
        return True if x == y else False


def main() -> None:
    # get 2 number from user
    x: int = int(input("What's x: ").strip())
    y: int = int(input("What's y: ").strip())

    # compare 2 number
    cmp: Statements = Statements()
    result: int = cmp.compare(x=x, y=y)

    if result == 1:
        print(f"{x} is greater than {y}.")
    elif result == -1:
        print(f"{x} is less than {y}.")
    else:
        print(f"{x} is equall to {y}.")

    if cmp.isequal(x=x, y=y):
        print("is equall.")
    else:
        print("not equall.")


if __name__ == "__main__":
    main()
