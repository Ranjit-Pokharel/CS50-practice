class Calculator:
    def __init__(
        self,
    ) -> None:
        pass

    def add(self, x: float, y: float) -> float:
        return x + y

    def square(self, x: float) -> float:
        return x * x


def main() -> None:
    # get x and y from user
    x: float = float(input("What's X: ").strip())
    y: float = float(input("What's Y: ").strip())

    # calculate result
    cal: Calculator = Calculator()
    print(f"add result: {cal.add(x=x, y=y)}")
    print(f"Square of {x}: {cal.square(x=x)}")


if __name__ == "__main__":
    main()
