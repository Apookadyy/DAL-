def start_quiz():
    print("\n📝 Quick Quiz")
    questions = {
        "What is the output of print(2 + 3)? ": "5",
        "Which keyword is used to define a function in Python? ": "def"
    }
    score = 0

    for q, a in questions.items():
        answer = input(q)
        if answer.lower() == a.lower():
            score += 1

    print(f"Your score: {score}/{len(questions)}")
