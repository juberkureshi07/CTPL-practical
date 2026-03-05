# Simple Multiple Choice Quiz Game

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"],
        "answer": "B"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    }
]

score = 0

print("🎉 Welcome to the Quiz Game!")
print("-----------------------------")

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.")

print("\n-----------------------------")
print(f"Your final score is: {score}/{len(questions)}")

if score == len(questions):
    print("🏆 Excellent! You got all questions right!")
elif score >= len(questions) // 2:
    print("👍 Good job!")
else:
    print("📚 Keep practicing!")                                                                                            