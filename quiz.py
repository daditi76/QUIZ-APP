import json
import random
import os

QUESTIONS_FILE = 'questions.json'
RESULTS_FILE = 'results.txt'

def load_questions():
    try:
        with open(QUESTIONS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Questions file not found.")
        return []

def ask_question(question_data):
    print(f"\n{question_data['question']}")
    options = question_data['options']
    random.shuffle(options)  # Shuffle options
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    answer = input("Your answer (1-4): ")
    try:
        return options[int(answer) - 1] == question_data['answer']
    except (ValueError, IndexError):
        return False

def save_result(name, score, total):
    with open(RESULTS_FILE, 'a') as file:
        file.write(f"{name} scored {score}/{total}\n")

def main():
    print("🎉 Welcome to the Quiz App! 🎉")
    name = input("Enter your name: ")
    
    questions = load_questions()
    if not questions:
        return

    score = 0
    for q in questions:
        if ask_question(q):
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect! The right answer was: {q['answer']}")

    print(f"\n{name}, your final score is: {score}/{len(questions)}")
    save_result(name, score, len(questions))

if __name__ == "__main__":
    main()
