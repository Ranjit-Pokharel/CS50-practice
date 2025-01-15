import cowsay
import sys

def main()-> None:
    if len(sys.argv) != 2:
        sys.exit("Usage: say.py <text>.")
    cowsay.cow("hello, " + sys.argv[1])

if __name__ == "__main__":
    main()

    