class Grade:
    def __init__(self, score:float=0.0)-> None:
        self.grade:str = "N/A"
        self.score:float = score

    def score_grade(self,)-> None:
        if self.score >= 90:
            self.grade = "A"
            return
        elif self.score >= 80:
            self.grade = "B"
            return
        elif self.score >= 70:
            self.grade = "C"
            return
        elif self.score >= 60:
            self.grade = "E"
            return
        
        self.grade = "F"
        return
    

def main()-> None:
    # get user score
    score:float = float(input("What's the score: ").strip())

    # grade the score
    grade:Grade = Grade(score)

    grade.score_grade()

    print(grade.grade)


if __name__ == "__main__":
    main()
