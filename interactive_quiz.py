
# Nepal General Knowledge Quiz
# Class Python Project

def run_quiz():

    # List of questions
    questions = [
        "What is the capital of Nepal?",
        "What is the national flower of Nepal?",
        "What is the national animal of Nepal?",
        "What is the highest mountain in Nepal?",
        "When is Constitution Day celebrated in Nepal?",
        "What is the lower house of Parliament called?",
        "What is the minimum voting age in Nepal?",
        "Who was the first President of Nepal?",
        "How many provinces are there in Nepal?",
        "What is the official language of Nepal?"
    ]

    # List of choices
    choices = [
        ["A. Pokhara", "B. Kathmandu",
         "C. Butwal", "D. Dharan"],

        ["A. Rose", "B. Lotus",
         "C. Rhododendron", "D. Sunflower"],

        ["A. Cow", "B. Tiger",
         "C. Elephant", "D. Horse"],

        ["A. Kanchenjunga", "B. Annapurna",
         "C. Mount Everest", "D. Dhaulagiri"],

        ["A. September 20", "B. January 1",
         "C. May 1", "D. December 25"],

        ["A. National Assembly",
         "B. House of Representatives",
         "C. Supreme Court", "D. Cabinet"],

        ["A. 16 years", "B. 17 years",
         "C. 18 years", "D. 21 years"],

        ["A. Ram Baran Yadav",
         "B. Bidhya Devi Bhandari",
         "C. Ram Chandra Poudel",
         "D. Girija Prasad Koirala"],

        ["A. 5", "B. 6", "C. 7", "D. 8"],

        ["A. Maithili", "B. Nepali",
         "C. Newari", "D. Bhojpuri"]
    ]

    # List of correct answers
    answers = [
        "B", "C", "A", "C", "A",
        "B", "C", "A", "C", "B"
    ]

    # Starting score
    score = 0

    # Welcome message
    print("=" * 40)
    print("      NEPAL GENERAL KNOWLEDGE QUIZ")
    print("=" * 40)

    print("Instructions:")
    print("1. There are 10 questions.")
    print("2. Each question has four options.")
    print("3. Enter A, B, C, or D.")
    print("4. Each correct answer gives 1 mark.")

    print("=" * 40)

    # Loop through all questions
    for i in range(len(questions)):

        print("\nQuestion", i + 1)
        print(questions[i])

        # Display the options
        for choice in choices[i]:
            print(choice)

        # Take the user's answer
        user_answer = input(
            "Enter your answer (A/B/C/D): "
        )

        user_answer = user_answer.strip().upper()

        # Check if the input is valid
        while user_answer not in ["A", "B", "C", "D"]:

            print("Invalid answer!")
            user_answer = input(
                "Please enter A, B, C, or D: "
            )

            user_answer = user_answer.strip().upper()

        # Check the answer
        if user_answer == answers[i]:

            print("Correct answer!")
            score = score + 1

        else:

            print("Wrong answer!")
            print("Correct answer is:", answers[i])

        print("-" * 40)

    # Calculate percentage
    total = len(questions)
    percentage = (score / total) * 100

    # Display the final result
    print("\n" + "=" * 40)
    print("             QUIZ RESULT")
    print("=" * 40)

    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Wrong Answers:", total - score)
    print("Final Score:", score, "/", total)
    print("Percentage:", percentage, "%")

    # Give feedback based on the score
    if score >= 8:

        print("Performance: Excellent!")

    elif score >= 5:

        print("Performance: Good job!")

    else:

        print("Performance: Keep practicing!")

    print("=" * 40)
    print("Thank you for playing the quiz!")
    print("=" * 40)


# Start the quiz program
if __name__ == "__main__":
    run_quiz()