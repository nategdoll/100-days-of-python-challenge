class LetterGrade:

    def letter_grade(self, percent):
        if percent >= 100:
            return "A+"
        elif percent >= 94.0:
            return "A"
        elif percent >= 90.0:
            return "A-"
        elif percent >= 88.0:
            return "B+"
        elif percent >= 84.0:
            return "B"
        elif percent >= 80.0:
            return "B-"
        elif percent >= 78.0:
            return "C+"
        elif percent >= 74.0:
            return "C"
        elif percent >= 70.0:
            return "C-"
        elif percent >= 68.0:
            return "D+"
        elif percent >= 64.0:
            return "D"
        elif percent >= 60.0:
            return "D-"
        else:
            return "F"

    def __init__(self, correct, total):
        self.score = correct/total * 100
        self.letter = self.letter_grade(self.score)