import random

def round_check(question):
# make sure that rounds is more than 0

    while True:
       error = "Please enter an integer more than or equal to 1"

       response = input(question)

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


def int_check(question):

   response = input(question)
   if response == "xxx":
       return response

   # make sure that the user enters an integer
   error = "Please enter an integer"

   while True:

        try:
            response = int(response)
            if response == int(response):
                return response

        except ValueError:
            print(error)
            return "error"



def yes_no(question):
    """Checks user response to a question in y/n, returns 'yes' or 'no '"""

    while True:

        response = input(question).lower()

        # check if the user says yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please answer yes/no")


def string_checker(question, valid_ans =("easy", "medium", "hard")):

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
    """Prints instructions"""

    print("""
    *** Instructions ****

    This quiz is on Linear equations
    (eg. "What is X if X + 5 = 10")
    
    Choose how many questions you want to answer, then choose the difficulty 
    
    Answer the questions correctly to get a higher score!
    
    """)


def explanation():
    """Explains how the difficulty scale works"""

    print("""
    *** Different Difficulties ****

    There are 3 difficulties
    
    Easy : This mode asks you addition and subtraction questions 
    
    Medium : This mode asks you multiplication and division questions 
    
    Hard : This mode asks combines Easy and Medium. It asks you addition, 
           subtraction, multiplication or division questions
    
    """)


def generate_linear_equation_add_sub_problem():
    variable_answer = 0
    # Generate random numbers
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operator = random.choice(['+', '-'])

    # Create the question
    problem = f"{num1} {operator} {num2}"
    # calculates answer
    answer = eval(problem)

    # make 1 of the variables unknown
    question = f" X {operator} {num2} = {answer}"
    question2 = f" {num1} {operator} X = {answer}"

   # pick which question to ask
    question_ask = random.choice ([question, question2])

    if question_ask == question:
        variable_answer = num1

    elif question_ask == question2:
        variable_answer = num2
    # return the question and answer
    return question_ask, variable_answer


def generate_linear_equation_divi_multi_problem():
    variable_answer = 0
    # Generate random numbers
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    operator = random.choice(['/', '*'])

    # make sure division will give whole numbers
    if operator == '/':
        # make num1 divisible by num2
        num1 = num1 * num2

    # Create the question
    problem = f"{num1} {operator} {num2}"
    # calculate the answer
    answer = eval(problem)

    # make 1 of the numbers unknown
    question = f" X {operator} {num2} = {answer}"
    question2 = f" {num1} {operator} X = {answer}"

    # pick which question to ask
    question_ask = random.choice ([question, question2])

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
end_game = "no"
feedback = ""
default_params = "no"
answers_correct = 0
answers_wrong = 0
questions_answered = 0
question_mode = "easy"
num_rounds = 0
user_answer = 0
var_ans = 0
quest = 0

game_history = []


# title
print("➕➖✖️➗ Welcome to my Math Quiz! ➕➖✖️➗")
print()


# ask the user if they want instructions (check they say yes/no)
want_instructions = yes_no("Do you want to see the instructions?: ")

# Display the instructions if the user wants to see them
if want_instructions == "yes":
    instructions()

# Ask the user for the number of rounds/infinite mode
num_rounds = round_check("\nEnter the amount of rounds or press <enter> for infinite: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# ask the user if they want to know how they can customize the quiz
want_explanation = yes_no("\nDo you want to know how the difficulty scale works?  ")
if want_explanation == "yes":
    explanation()

# asks if they want to customize the quiz
default_params = yes_no("\nThe default difficulty is set to easy"
                        "\nDo you want to use the default difficulty?  ")
# set mode to easy if yes
if default_params == "yes":
    question_mode = "easy"

# allow user to choose the quiz difficulty
else:
    question_mode = string_checker("\nPlease choose which difficulty you would like to use:  ")


# Game loop starts here
while rounds_played < num_rounds:

    # rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\nQuestion {rounds_played + 1} (Infinite Mode)"
    else:
        rounds_heading = f"\nQuestion {rounds_played + 1} of {num_rounds}"

    print(rounds_heading)

    # asks easy question if mode is set to easy
    if question_mode == "easy":
        quest, var_ans = generate_linear_equation_add_sub_problem()

        # asks the user the questions
        user_answer = int_check(f"What is {quest}? ")

        while user_answer == "error":
            user_answer = int_check(f"What is {quest}? ")

        # checks if the user answer is the correct answer
        if user_answer == var_ans:
            print("Correct!")
        # checks if the user wants to exit and breaks loop if yes
        elif user_answer == "xxx":
            end_game = "yes"
            break
        # shows what the answer is
        else:
            print(f"Wrong! The answer is {var_ans}")


    # asks medium question if on medium mode
    elif question_mode == "medium":
        quest, var_ans = generate_linear_equation_divi_multi_problem()

        # asks the user the questions
        user_answer = int_check(f"What is {quest}? ")

        while user_answer == "error":
            user_answer = int_check(f"What is {quest}? ")

        # checks if the user answer is the correct answer
        if user_answer == var_ans:
            print("Correct!")
        # checks if the user wants to exit and breaks loop if yes
        elif user_answer == "xxx":
            end_game = "yes"
            break
        # shows what the answer is
        else:
            print(f"Wrong! The answer is {var_ans}")


    # asks hard questions if on hard mode
    elif question_mode == "hard":
        quest, var_ans = random.choice([generate_linear_equation_add_sub_problem(),
                                        generate_linear_equation_divi_multi_problem()])

        # asks the user the questions
        user_answer = int_check(f"What is {quest}? ")

        while user_answer == "error":
            user_answer = int_check(f"What is {quest}? ")

        # checks if the user answer is the correct answer
        if user_answer == var_ans:
            print("Correct!")
        # checks if the user wants to exit and breaks loop if yes
        elif user_answer == "xxx":
            end_game = "yes"
            break
        # shows what the answer is
        else:
            print(f"Wrong! The answer is {var_ans}")



    # adds one to the number of questions answered
    questions_answered += 1

    # check if the answer is correct and adds 1 to answers correct or to answers wrong
    if user_answer == var_ans:
        answers_correct +=1
    else:
        answers_wrong +=1

    # if user has entered the exit code end the game!!
    if end_game == "yes":
        break

    # adds 1 to rounds played
    rounds_played += 1

    # if users are in infinite mode add more rounds
    if mode == "infinite":
        num_rounds += 1


    # add round result to game history
    history_feedback = f"Round: {rounds_played}  Question: {quest}  Correct Answer: {var_ans}  Your answer: {user_answer}"
    game_history.append(history_feedback)


# check users have played at least 1 round before calculating stats
if rounds_played > 0:
    questions_correct = answers_correct
    questions_wrong = answers_wrong
    percent_correct = questions_correct / rounds_played * 100
    percent_wrong = 100 - percent_correct

    # output game stats
    print("\n📊📊📊 Game Statistics 📊📊📊")
    print(f"🥳 Questions Correct: {questions_correct} ({percent_correct:.2f}%) \t "
          f"😭 Questions Wrong : {questions_wrong} ({percent_wrong:.2f}%) \t")

    # display the game history on request
    # ask the user if they want to see their game history and output if answer is yes
    see_history = yes_no("\nDo you want to see your game history? ")
    if see_history == "yes":

        # game history
        print("\n📜📜📜Game History📜📜📜")
        print()
        for item in game_history:
            print(item)

    # end
    print("\nThanks for playing!")

