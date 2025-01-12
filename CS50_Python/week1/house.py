def main()-> None:
    name:str = input("Name: ").strip()

    print(house(name=name))


def house(name:str)-> str:
    name = name.lower()
    match name:
        case "harry" | "hermione" | "ron":
            return "Gryffindor"
        case "draco":
            return "Slytherin"
        case _:
            return "Who?"


if __name__ == "__main__":
    main()