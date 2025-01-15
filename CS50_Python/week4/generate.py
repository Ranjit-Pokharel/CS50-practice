import random

def main()-> None:
    coin_faces = ["heads", "tails"]
    coin:str = get_valid_face("Heads or Tail: ", coin_faces)
    choice:str = random.choice(["heads", "tails"])

    if coin == choice:
        print("You win")
    else:
        print("you loss")



def get_valid_face(prompt:str, valid_lists: list[str])-> str:
    while True:
        try:
            face:str = input(prompt).lower()
            for valid_list in valid_lists:
                if face == valid_list:
                    return face
            raise ValueError
        except ValueError:
            print(f"choice {valid_lists}")
            pass


if __name__ == "__main__":
    main()