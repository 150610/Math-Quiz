import random


def int_check(question):
    """Checks for Integer Answers"""

    while True:

        response = input(question)

        if num_rounds == 0:
            error = "Please enter an integer more than 0"

            # check for infinite mode
            if response == "":
                return "infinite"

            try:
                response = int(response)

                if response < 1:
                    print(error)
                    continue
                else:
                    return response
            except ValueError:
                print(error)
                continue


        else:

         # # check exit code
            if response == "xxx":
                return response

            # make sure that the user enters an integer
            error = "Please enter an integer"

            try:
                response = int(response)
                if response == int(response):
                    return response

            except ValueError:
                print(error)
                return "error"


def string_checker(question, valid_ans =("yes", "no")):
    """Checks for String Answers"""

    error = f"Please enter a valid response from the following list: {valid_ans}"

    while True:

        # get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            #check if the user response is in the word list
            if item == user_response:
                return item

            #check if the user response is the same as the
            # #first letter of an item in the list
            elif user_response == item[0]:
                return item

        #print error if the user does not enter a valid response
        print(error)
        print()


def instructions():
    """Prints instructions/explanation"""

    if want_instructions == "yes":
         print("""
        *** Instructions ****
    
        This quiz is on Linear equations
        (eg. "What is X if X + 5 = 10")
    
        Choose how many questions you want to answer, then choose the difficulty 
    
        Answer the questions correctly to get a higher score!
    
        
       *** Different Difficulties ****

       There are 3 difficulties

       Easy : This mode asks you addition and subtraction questions 

       Medium : This mode asks you multiplication and division questions 

       Hard : This mode asks combines Easy and Medium. It asks you addition, 
              subtraction, multiplication or division questions

       """)


def generate_linear_equation_problem():
    """Generates Linear Equations"""
    variable_answer = 0
    num1 = 5
    operator = "+"
    num2 = 5
    question_choice = "easy"

    # asks questions based on mode
    if question_mode == "easy":
        question_choice = "easy"
    elif question_mode == "medium":
        question_choice = "medium"

    elif question_mode == "hard":
        #pick whether question is easy or medium
        question_choice = random.choice (["easy", "medium"])

    if question_choice == "easy":
       # Generate random numbers
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        operator = random.choice(['+', '-'])
    elif question_choice == "medium":
         #Generate random numbers
        num1 = random.randint(1, 12)
        num2 = random.randint(1, 12)
        operator = random.choice(['/', '*'])

    # make sure division will give whole numbers
    if operator == '/':
        # make num1 divisible by num2
        num1 = num1 * num2

    # Create the question
    problem = f"{num1} {operator} {num2}"
    # calculates answer
    answer = eval(problem)

    # make 1 of the variables unknown
    question = f" X {operator} {num2} = {answer}"
    question2 = f" {num1} {operator} X = {answer}"

    # pick which question to ask
    question_ask = random.choice([question, question2])

    # make the answer the missing variable
    if question_ask == question:
        variable_answer = num1
    elif question_ask == question2:
        variable_answer = num2

    # return the question and answer
    return question_ask, variable_answer



# Main routine starts here

# Initialise game variables
mode = "regular"
rounds_played = 0
answers_correct = 0
answers_wrong = 0
questions_answered = 0
num_rounds = 0

quiz_history = []
difficulty_list = ["easy", "medium", "hard"]

# title
print("➕➖✖️➗ Welcome to my Math Quiz! ➕➖✖️➗")
print()

# ask the user if they want instructions (check they say yes/no)
want_instructions = string_checker("Do you want to see the instructions?: ")

# Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()

# Ask the user for the number of rounds/infinite mode
num_rounds = int_check("\nEnter the amount of rounds or press <enter> for infinite: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# asks if they want to customize the quiz
default_params = string_checker("\nThe default difficulty is set to easy"
                        "\nDo you want to use the default difficulty?  ")
# set mode to easy if yes
if default_params == "yes":
    question_mode = "easy"

# allow user to choose the quiz difficulty
else:
    question_mode = string_checker("\nPlease choose which difficulty you would like to use:  ", difficulty_list)

# Game loop starts here
while rounds_played < num_rounds:

    # rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\nQuestion {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\nQuestion {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)

    # generates question
    quest, var_ans = generate_linear_equation_problem()

    # asks the user the questions
    user_answer = int_check(f"What is {quest}? ")

    while user_answer == "error":
        user_answer = int_check(f"What is {quest}? ")

    # checks if the user answer is the correct answer
    if user_answer == var_ans:
        print("Correct!")
    # checks if the user wants to exit and breaks loop if yes
    elif user_answer == "xxx":
        break
    # shows what the answer is
    else:
        print(f"Wrong! The answer is {var_ans}")

    # adds one to the number of questions answered
    questions_answered += 1

    # check if the answer is correct and adds 1 to answers correct or to answers wrong
    if user_answer == var_ans:
        answers_correct += 1
    else:
        answers_wrong += 1

    # adds 1 to rounds played
    rounds_played += 1

    # if users are in infinite mode add more rounds
    if mode == "infinite":
        num_rounds += 1

    # add round result to quiz history
    history_feedback = f"Round: {rounds_played}  Question: {quest}  Correct Answer: {var_ans}  Your answer: {user_answer}"
    quiz_history.append(history_feedback)

# check users have played at least 1 round before calculating stats
if rounds_played > 0:
    questions_correct = answers_correct
    questions_wrong = answers_wrong
    percent_correct = questions_correct / rounds_played * 100
    percent_wrong = 100 - percent_correct

    # output quiz stats
    print("\n📊📊📊 Quiz Statistics 📊📊📊")
    print(f"🥳 Questions Correct: {questions_correct} ({percent_correct:.2f}%) \t "
          f"😭 Questions Wrong : {questions_wrong} ({percent_wrong:.2f}%) \t")

    # display the quiz history on request
    # ask the user if they want to see their quiz history and output if answer is yes
    see_history = string_checker("\nDo you want to see your quiz history? ")
    if see_history == "yes":

        # quiz history
        print("\n📜📜📜 Quiz History 📜📜📜")
        print()
        for item in quiz_history:
            print(item)

    # end
    print("\nThanks for playing!")

if rounds_played == 0:
    print("\nYou chickened out, and did not play any rounds 🐔")