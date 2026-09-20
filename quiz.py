import sys
import time
from typing import Dict, List, Tuple, Any

def get_quiz_questions() -> List[Dict[str, Any]]:
    return [
        {
            "id": 1,
            "question": "Which of the following data types is immutable in Python?",
            "options": {
                "A": "List",
                "B": "Dictionary",
                "C": "Tuple",
                "D": "Set"
            },
            "answer": "C",
            "explanation": "Tuples cannot be modified after creation, making them immutable in Python."
        },
        {
            "id": 2,
            "question": "What is the output of bool([]) in Python?",
            "options": {
                "A": "True",
                "B": "False",
                "C": "None",
                "D": "TypeError"
            },
            "answer": "B",
            "explanation": "An empty list evaluates to False in a boolean context."
        },
        {
            "id": 3,
            "question": "Which keyword is used to create a generator function in Python?",
            "options": {
                "A": "return",
                "B": "generate",
                "C": "yield",
                "D": "produce"
            },
            "answer": "C",
            "explanation": "The yield keyword is used in generator functions."
        },
        {
            "id": 4,
            "question": "How do you open a file for reading and writing without truncating it?",
            "options": {
                "A": "w+",
                "B": "r+",
                "C": "a",
                "D": "rw"
            },
            "answer": "B",
            "explanation": "'r+' opens a file for both reading and writing without truncating it."
        },
        {
            "id": 5,
            "question": "What is the average time complexity of looking up a key in a Python dictionary?",
            "options": {
                "A": "O(1)",
                "B": "O(n)",
                "C": "O(log n)",
                "D": "O(n^2)"
            },
            "answer": "A",
            "explanation": "Python dictionaries use hash tables, giving average O(1) lookup time."
        },
        {
            "id": 6,
            "question": "What does the pass statement do in Python?",
            "options": {
                "A": "Skips the current loop iteration",
                "B": "Exits the current function",
                "C": "Serves as a placeholder",
                "D": "Passes control to an exception handler"
            },
            "answer": "C",
            "explanation": "pass is a placeholder statement that performs no action."
        }
    ]

def display_welcome_banner() -> None:
    divider = "=" * 60
    print("\n" + divider)
    print("           WELCOME TO THE PYTHON QUIZ MASTER")
    print("          Test Your Knowledge & Core Concepts")
    print(divider)
    print("Instructions:")
    print("  Read each question carefully.")
    print("  Type A, B, C, or D to submit your answer.")
    print("  Your final score will appear at the end.")
    print(divider + "\n")

def display_question(index: int, total: int, question_data: Dict[str, Any]) -> None:
    print(f"\n[Question {index} of {total}]")
    print(question_data["question"])
    print()
    for option_key, option_text in question_data["options"].items():
        print(f"  [{option_key}] {option_text}")
    print()

def get_user_choice(valid_options: List[str]) -> str:
    prompt = f" Your answer ({'/'.join(valid_options)}): "
    while True:
        try:
            user_input = input(prompt).strip().upper()
        except (KeyboardInterrupt, EOFError):
            print("\nQuiz cancelled. Goodbye!")
            sys.exit(0)
        if not user_input:
            print("! Input cannot be empty.")
        elif user_input not in valid_options:
            print(f"! Invalid choice. Please choose: {', '.join(valid_options)}")
        else:
            return user_input

def evaluate_answer(user_choice: str, correct_answer: str) -> bool:
    return user_choice == correct_answer

def calculate_score(correct_answers: int, total_questions: int) -> Tuple[float, str, str]:
    if total_questions == 0:
        return 0.0, "N/A", "No questions were completed."
    percentage = (correct_answers / total_questions) * 100
    if percentage >= 90:
        rating = "Outstanding"
        feedback = "Excellent work! You have a strong understanding of Python."
    elif percentage >= 75:
        rating = "Proficient"
        feedback = "Well done! You have a solid Python foundation."
    elif percentage >= 50:
        rating = "Competent"
        feedback = "Good effort. Review the topics you missed."
    else:
        rating = "Needs Practice"
        feedback = "Keep practicing Python and improve step by step."
    return round(percentage, 1), rating, feedback

def display_results_summary(
    score: int,
    total: int,
    percentage: float,
    rating: str,
    feedback: str,
    history: List[Dict[str, Any]]
) -> None:
    border = "=" * 60
    print("\n" + border)
    print("                    QUIZ RESULTS")
    print(border)
    print(f"Score: {score} / {total}")
    print(f"Percentage: {percentage}%")
    print(f"Rating: {rating}")
    print(f"Assessment: {feedback}")
    print(border)
    print("\nDETAILED QUESTION BREAKDOWN:")
    print("-" * 60)
    for record in history:
        status = "✓ CORRECT" if record["is_correct"] else "X INCORRECT"
        print(f"\nQ{record['number']}: {record['question']}")
        print(f"Your Answer: [{record['user_choice']}] {record['options'][record['user_choice']]}")
        print(f"Correct Answer: [{record['correct_answer']}] {record['options'][record['correct_answer']]}")
        print(f"Result: {status}")
        print(f"Explanation: {record['explanation']}")
    print("\n" + border)

def ask_play_again() -> bool:
    while True:
        try:
            choice = input("\nWould you like to take the quiz again? (Y/N): ").strip().upper()
        except (KeyboardInterrupt, EOFError):
            return False
        if choice in ("Y", "YES"):
            return True
        elif choice in ("N", "NO"):
            return False
        else:
            print("Please enter Y or N.")

def run_quiz() -> None:
    display_welcome_banner()
    questions = get_quiz_questions()
    total_questions = len(questions)
    score = 0
    history = []
    
    for index, question in enumerate(questions, start=1):
        display_question(index, total_questions, question)
        valid_keys = list(question["options"].keys())
        user_choice = get_user_choice(valid_keys)
        is_correct = evaluate_answer(user_choice, question["answer"])
        
        if is_correct:
            score += 1
            print("✓ Correct!\n")
        else:
            correct_answer = question["answer"]
            correct_text = question["options"][correct_answer]
            print(f"X Incorrect. The correct answer was [{correct_answer}] {correct_text}\n")
            
        history.append({
            "number": index,
            "question": question["question"],
            "options": question["options"],
            "user_choice": user_choice,
            "correct_answer": question["answer"],
            "is_correct": is_correct,
            "explanation": question["explanation"]
        })
        time.sleep(0.3)
        
    percentage, rating, feedback = calculate_score(score, total_questions)
    display_results_summary(score, total_questions, percentage, rating, feedback, history)

def main() -> None:
    while True:
        run_quiz()
        if not ask_play_again():
            print("\nThank you for playing the Python Quiz Game!")
            print("Happy coding!\n")
            break

if __name__ == "__main__":
    main()
