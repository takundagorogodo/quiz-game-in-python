print("""
************************************************************
        Welcome to My Quiz Game Of Python OPP Concepts
************************************************************
""")

# Questions and Answers
quiz = [
    {"text":"The ability of one class to acquire methods and attributes of another class is called?",
     "options":["A. Inheritance", "B. Abstraction", "C. Polymorphism", "D. Object"], 
     "answer":"A"},

    {"text":"Which of the following is a type of inheritance?",
     "options":["A. Single", "B. Double", "C. Multiple", "D. Both A and C"],
      "answer":"D"},

    {"text":"What type of inheritance has multiple subclasses to a single superclass?",
     "options":["A. Multiple Inheritance", "B. Multilevel Inheritance", "C. Hierarchical Inheritance", "D. None of these"], 
     "answer":"C"},

    {"text":"What is the depth of multi-level inheritance in Python?",
     "options":["A. Two level", "B. Three level", "C. Any level", "D. None of these"], 
     "answer":"C"},

    {"text":"What does MRO stand for?",
     "options":["A. Method Recursive Object", "B. Method Resolution Order", "C. Main Resolution Order", "D. Method Resolution Object"], 
     "answer":"B"},

    {"text":"Which keyword is used to define a function in Python?",
     "options":["A. func", "B. define", "C. def", "D. function"], 
     "answer":"C"},

    {"text":"Which of the following is mutable in Python?",
     "options":["A. Tuple", "B. String", "C. List", "D. FrozenSet"], 
     "answer":"C"},

    {"text":"Which operator is used for exponentiation in Python?",
     "options":["A. ^", "B. **", "C. %", "D. //"], 
     "answer":"B"},

    {"text":"Which of these is a Python tuple?",
     "options":["A. [1,2,3]", "B. {1,2,3}", "C. (1,2,3)", "D. <1,2,3>"], 
     "answer":"C"},

    {"text":"What is the output of: print(2 * 3 ** 2)?",
     "options":["A. 36", "B. 18", "C. 12", "D. 32"], 
     "answer":"B"},

    {"text":"Which of these data types is not built-in in Python?",
     "options":["A. list", "B. dict", "C. class", "D. tuple"], 
     "answer":"C"},

    {"text":"Which keyword is used to create a class in Python?",
     "options":["A. class", "B. def", "C. object", "D. module"], 
     "answer":"A"},

    {"text":"Which function is used to get the length of a string in Python?",
     "options":["A. len()", "B. size()", "C. length()", "D. count()"], 
     "answer":"A"},

    {"text":"What is the output of: print(bool(0))?",
     "options":["A. True", "B. False", "C. 0", "D. None"], 
     "answer":"B"},

    {"text":"Which of these is a Python set?",
     "options":["A. {1,2,3}", "B. [1,2,3]", "C. (1,2,3)", "D. <1,2,3>"], 
     "answer":"A"},

    {"text":"Which method adds an element to the end of a list?",
     "options":["A. add()", "B. append()", "C. insert()", "D. extend()"], 
     "answer":"B"},

    {"text":"Which keyword is used for exception handling in Python?",
     "options":["A. try-except", "B. handle", "C. catch", "D. error"], 
     "answer":"A"},

    {"text":"What is the output of: print(10 // 3)?",
     "options":["A. 3.33", "B. 3", "C. 3.0", "D. 4"], 
     "answer":"B"},

    {"text":"Which of these is a Python dictionary?",
     "options":["A. {‘key’:‘value’}", "B. [‘key’,‘value’]", "C. (‘key’,‘value’)", "D. <‘key’,‘value’>"], 
     "answer":"A"},

    {"text":"Which built-in Python function returns the largest number?",
     "options":["A. max()", "B. top()", "C. largest()", "D. high()"], 
     "answer":"A"}
]

# Initialize score
score = 0

# Function to check answers
def check_answer(user_guess, correct_answer):
    return user_guess == correct_answer

# Quiz Loop
for index, question in enumerate(quiz):
    print("\n*******************************")
    print(f"Q{index+1}: {question['text']}")
    for option in question["options"]:
        print(option)

    guess = input("Enter your answer (A/B/C/D): ").upper()

    if check_answer(guess, question["answer"]):
        print("✅ Correct Answer")
        score += 1
    else:
        print("❌ Incorrect Answer")
        print(f"The correct answer is {question['answer']}")

    print(f"Your current score is {score}/{index + 1}")

# Final Results
print("\n*****************************************")
print(f"You answered {score} out of {len(quiz)} questions correctly.")
percentage = (score / len(quiz)) * 100
print(f"Your score is {percentage:.2f}%")
print("*****************************************")
