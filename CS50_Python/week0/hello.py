class Greet:

    def __init__(self, name: str = "world") -> None:
        # filter user input
        self.name: str = name.strip().title()

    def hello(
        self,
    ) -> str:
        return f"Hello, {self.name}!"


def main() -> None:
    # Ask user for name
    name: str = input("Whst's your name? ")
    greet: Greet = Greet(name=name)

    # greet the user with their name
    print(greet.hello())


if __name__ == "__main__":
    main()
