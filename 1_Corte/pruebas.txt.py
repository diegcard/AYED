class Contest:
    def __init__(self, name, problems):
        self.name = name
        self.problems = problems
        self.submissions = []

    def add_submission(self, submission):
        self.submissions.append(submission)

    def get_winners(self):
        scores = {}
        for submission in self.submissions:
            if submission.username not in scores:
                scores[submission.username] = 0
            scores[submission.username] += submission.score
        sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [username for username, score in sorted_scores]


class Submission:
    def __init__(self, username, problem_name, score):
        self.username = username
        self.problem_name = problem_name
        self.score = score


def main():
    # Inicializar el concurso con algunos problemas
    contest = Contest("Programming Competition", ["Problem 1", "Problem 2", "Problem 3"])

    while True:
        print("1. Add Submission")
        print("2. Show Winners")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            username = input("Enter username: ")
            problem_name = input("Enter problem name: ")
            score = int(input("Enter score: "))
            contest.add_submission(Submission(username, problem_name, score))
        elif choice == 2:
            print("Winners:", contest.get_winners())
        elif choice == 3:
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == '__main__':
    main()
