def main()-> None:
    size:int = get_size()
    print_square(size=size)


def get_size()-> int:
    while True:
        size:int = int(input("What is the size: "))

        if size > 0:
            return size
        
def print_square(size:int)-> None:
    for i in range(size):
        print_row(width=size)


def print_row(width:int)-> None:
    print("#" * width)

if __name__ == "__main__":
    main()