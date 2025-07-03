import random
import time

class Question:
    def __init__(self, prompt, choices, answer):  # fixed: __init__ not _init_
        self.prompt = prompt
        self.choices = choices
        self.answer = answer  # answer is the index (int) of the correct choice

class QuizGame:
    def __init__(self, questions, timer_per_question=15):  # fixed: __init__ not _init_
        self.questions = questions
        self.score = 0
        self.timer_per_question = timer_per_question
        self.review = []

    def ask_question(self, question):
        print("\n" + question.prompt)
        for idx, choice in enumerate(question.choices):
            print(f"{idx + 1}. {choice}")
        start_time = time.time()
        try:
            user_input = input(f"Your answer (1-{len(question.choices)}) [You have {self.timer_per_question} seconds]: ")
            time_taken = time.time() - start_time
            if time_taken > self.timer_per_question:
                print("Time's up!")
                self.review.append((question, None))
                return False
            answer = int(user_input) - 1
            if answer == question.answer:
                print("Correct!")
                self.score += 1
                self.review.append((question, answer))
                return True
            else:
                print(f"Incorrect. The correct answer was: {question.choices[question.answer]}")
                self.review.append((question, answer))
                return False
        except (ValueError, IndexError):
            print("Invalid input.")
            self.review.append((question, None))
            return False

    def start(self):
        print("Welcome to the Quiz Game!")
        random.shuffle(self.questions)
        for q in self.questions:
            self.ask_question(q)
        print(f"\nQuiz Over! Your final score is: {self.score}/{len(self.questions)}")
        self.show_review()

    def show_review(self):
        print("\n--- Answer Review ---")
        for i, (q, user_answer) in enumerate(self.review):
            print(f"Q{i + 1}: {q.prompt}")
            for idx, choice in enumerate(q.choices):
                indicator = ""
                if idx == q.answer:
                    indicator = " (Correct)"
                elif user_answer == idx:
                    indicator = " (Your Answer)"
                print(f"  {idx + 1}. {choice}{indicator}")
            if user_answer is None:
                print("  No answer provided or timed out.")
            print()

# Run the game
if __name__ == "__main__": 
    question_list = [
        Question(
            "What is the capital of France?",
            ["Berlin", "London", "Paris", "Madrid"],
            2
        ),
        Question(
            "Which language is primarily used for Android development?",
            ["Swift", "Kotlin", "JavaScript", "Ruby"],
            1
        ),
        Question(
            "Which planet is known as the Red Planet?",
            ["Earth", "Mars", "Jupiter", "Saturn"],
            1
        ),
        Question(
            "Who wrote the play 'Romeo and Juliet'?",
            ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
            0
        )
    ]
    
    game = QuizGame(question_list, timer_per_question=20)
    game.start()
