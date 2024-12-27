import random;
import time;
print("Welcome to the Programming Quiz!")

questions = [
    {
        "question": "What does HTML stand for?",
        "options": ["1. Hyper Text Markup Language", 
                    "2. High Text Machine Learning", 
                    "3. Hyperlink and Text Marking Language", 
                    "4. Home Tool Markup Language"],
        "answer": 1
    },
    {
        "question": "Which language is used for data science?",
        "options": ["1. C++", "2. Python", "3. Java", "4. HTML"],
        "answer": 2
    },
    {
        "question": "Who created this games?",
        "options": ["1. idk", "2. Krisha", "3. someone", "4. Another one"],
        "answer": 2
    }
]
random.shuffle(questions)
time.sleep(0.5)
score = 0
for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)
    
    user_answer = int(input("Enter the number of your answer: "))
    if user_answer == q["answer"]:
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong! 😔")

print(f"\nYour final score is: {score}/{len(questions)}")

