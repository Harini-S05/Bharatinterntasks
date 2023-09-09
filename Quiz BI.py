import tkinter as tk

class SimpleQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Quiz App")
        
        # Set the background color
        self.root.configure(bg='lightblue')

        self.question_number = 0
        self.score = 0

        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["Paris", "London", "Berlin", "Madrid"],
                "correct_option": 0,
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Mars", "Venus", "Jupiter"],
                "correct_option": 1,
            },
            {
                "question": "What is the largest mammal?",
                "options": ["Elephant", "Giraffe", "Whale", "Kangaroo"],
                "correct_option": 2,
            },
        ]

        self.question_label = tk.Label(root, text="", bg='lightblue')
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.score_label = tk.Label(root, text="Score: 0", bg='lightblue')
        self.score_label.pack(pady=10)
        
        # Create a label for displaying the total score
        self.total_score_label = tk.Label(root, text="", bg='lightblue')
        self.total_score_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.question_number < len(self.questions):
            question_data = self.questions[self.question_number]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
            self.question_number += 1
        else:
            self.question_label.config(text="Quiz finished!")
            for button in self.option_buttons:
                button.config(state=tk.DISABLED)
            
            # Display the total score
            self.total_score_label.config(text=f"Total Score: {self.score}")

    def check_answer(self, selected_option):
        question_data = self.questions[self.question_number - 1]
        correct_option = question_data["correct_option"]
        if selected_option == correct_option:
            self.score += 1
        self.score_label.config(text=f"Score: {self.score}")
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleQuizApp(root)
    root.mainloop()
