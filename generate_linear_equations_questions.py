import random


def generate_linear_equation_add_sub_problem():
    # Generate random numbers
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operator = random.choice(['+', '-'])

    # Create the question and calculate answer
    problem = f"{num1} {operator} {num2}"
    # eval() calculates string expressions
    answer = eval(problem)

    question = f" X {operator} {num2} = {answer}"
    question2 = f" {num1} {operator} X = {answer}"
    question_ask = random.choice ([question, question2])

    if question_ask == question:
        variable_answer = num1

    elif question_ask == question2:
        variable_answer = num2

    return question_ask, variable_answer



def generate_linear_equation_divi_multi_problem():
    # Generate random numbers
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    operator = random.choice(['/', '*'])

    # make sure division will give whole numbers
    if operator == '/':
        # make num1 divisible by num2
        num1 = num1 * num2

    # Create the question and calculate answer
    problem = f"{num1} {operator} {num2}"
    # eval() calculates string expressions
    answer = eval(problem)

    question = f" X {operator} {num2} = {answer}"
    question2 = f" {num1} {operator} X = {answer}"
    question_ask = random.choice ([question, question2])

    if question_ask == question:
        variable_answer = num1

    elif question_ask == question2:
        variable_answer = num2

    return question_ask, variable_answer



# test question for add/sub equation
quest, var_ans = generate_linear_equation_add_sub_problem()
user_answer = int(input(f"What is {quest}? "))

if user_answer == var_ans:
    print("Correct!")
else:
    print(f"Wrong. The answer is {var_ans}")

# test question for divi/multi equation
quest, var_ans = generate_linear_equation_divi_multi_problem()
user_answer = int(input(f"What is {quest}? "))

if user_answer == var_ans:
    print("Correct!")
else:
    print(f"Wrong. The answer is {var_ans}")

