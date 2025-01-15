import statistics

def main()-> None:
    scores:list[int] = get_score()
    print(statistics.mean(scores))

def get_score()-> list[int]:
    while True:
        try:
            num:int = int(input("Number of score: "))
            break
        except ValueError:
            print("Enter valid number.")
            pass
    scores:list = []
    for i, _ in enumerate(range(num), start=1):
        while True:
            try:
                score:int = int(input(f"{i}. score: "))
                scores.append(score)
                break
            except ValueError:
                print("Enter valid score.")
                continue
    return scores

if __name__ == "__main__":
    main()