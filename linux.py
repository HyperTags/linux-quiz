#!/usr/bin/env python3
import os
import sys
from termcolor import colored


class LinuxFundamentalsQuiz:
    def __init__(self):
        self.score = 0
        self.questions = self.load_questions()
        self.total_questions = len(self.questions)

    def load_questions(self):
        return [
            {
                "question": "1. Which command lists files in a directory, including hidden ones?",
                "options": ["a) ls", "b) ls -a", "c) list -all"],
                "answer": "b",
                "explanation": "'ls -a' shows all files, including hidden ones (starting with .)",
            },
            {
                "question": "2. What does 'chmod 755 filename' do?",
                "options": [
                    "a) Owner: rwx, Group: r-x, Others: r-x",
                    "b) Owner: rw-, Group: r--, Others: r--",
                    "c) Owner: rwx, Group: rwx, Others: rwx",
                ],
                "answer": "a",
                "explanation": "755 = Owner: 7 (rwx), Group: 5 (r-x), Others: 5 (r-x)",
            },
            {
                "question": "3. Which command shows your current directory?",
                "options": ["a) pwd", "b) cwd", "c) where"],
                "answer": "a",
                "explanation": "'pwd' stands for 'print working directory'",
            },
            {
                "question": "4. How to find files modified in last 24 hours?",
                "options": [
                    "a) find -mtime -1",
                    "b) find -newer 1day",
                    "c) ls --recent",
                ],
                "answer": "a",
                "explanation": "'-mtime -1' means modified less than 1 day ago",
            },
            {
                "question": "5. What does 'grep' do?",
                "options": [
                    "a) Search for patterns in files",
                    "b) Group files by extension",
                    "c) Create new user group",
                ],
                "answer": "a",
                "explanation": "grep = Global Regular Expression Print",
            },
            {
                "question": "6. How to get help about 'mkdir' command?",
                "options": ["a) help mkdir", "b) mkdir --help", "c) Both a and b"],
                "answer": "c",
                "explanation": "Most commands accept --help flag and 'help' works for shell builtins",
            },
        ]

    def clear_screen(self):
        os.system("clear" if os.name == "posix" else "cls")

    def display_header(self):
        self.clear_screen()
        print(colored("=== Linux Fundamentals Quiz ===", "cyan", attrs=["bold"]))
        print(colored(f"Questions: {self.total_questions}", "yellow"))
        print("----------------------------------------\n")

    def run_quiz(self):
        self.display_header()
        print(colored("Test your Linux knowledge! Answer with a, b, or c.\n", "green"))

        for q in self.questions:
            print(colored(q["question"], "white", attrs=["bold"]))
            for option in q["options"]:
                print(colored(option, "yellow"))

            while True:
                try:
                    user_answer = input("\nYour answer: ").lower().strip()
                    if user_answer in ["a", "b", "c"]:
                        break
                    print(colored("Invalid! Enter a, b, or c.", "red"))
                except KeyboardInterrupt:
                    print("\n\nQuiz interrupted. Goodbye!")
                    sys.exit(0)

            if user_answer == q["answer"]:
                self.score += 1
                print(colored("\n✓ Correct!", "green"))
            else:
                print(colored(f"\n✗ Incorrect. Correct answer is {q['answer']}", "red"))

            print(colored(f"Explanation: {q['explanation']}", "blue"))
            input("\nPress Enter to continue...")
            self.display_header()

        self.show_results()

    def show_results(self):
        percentage = (self.score / self.total_questions) * 100
        print(colored("=== Quiz Results ===", "cyan", attrs=["bold"]))
        print(colored(f"Final Score: {self.score}/{self.total_questions}", "yellow"))
        print(colored(f"Percentage: {percentage:.1f}%", "yellow"))

        if percentage >= 85:
            print(colored("\nExcellent! Linux pro detected!", "green", attrs=["bold"]))
        elif percentage >= 60:
            print(colored("\nGood job! You know your basics.", "blue"))
        else:
            print(colored("\nKeep practicing! Review Linux fundamentals.", "red"))

        print("\nThanks for taking the quiz!")


if __name__ == "__main__":
    try:
        quiz = LinuxFundamentalsQuiz()
        quiz.run_quiz()
    except KeyboardInterrupt:
        print("\n\nQuiz aborted. Goodbye!")
        sys.exit(0)
