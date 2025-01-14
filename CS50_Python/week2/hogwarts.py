def main()-> None:
    students = [
        {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None},
    ]

    name: str = get_user(student_lists=students)
    show_student_detail(student_lists=students, name=name)


def get_user(student_lists: list[dict[str, str]])-> str:
    while True:
        name: str = input("What's the Name: ").strip().title()

        for data in student_lists:
            if name == data["name"]:
                return name


def show_student_detail(student_lists: list[dict[str, str]], name: str)-> None:
    for student in student_lists:
        if name == student["name"]:
            print(student["name"], student["house"], student["patronus"], sep=", ")
            return
    print("N/A")
    return

if __name__ == "__main__":
    main()

