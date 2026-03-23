import random


def generate_basic_add_sub_problem():
    # Generate random numbers
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    operator = random.choice(['+', '-'])

    # Create the question and calculate answer
    question = f"{num1} {operator} {num2}"
    # eval() calculates string expressions
    answer = eval(question)

    return question, answer

def generate_basic_division_problem():
    # Generate random numbers
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = '/'

    # make sure division will give whole numbers
    if operator == '/':
        # make num1 divisible by num2
        num1 = num1 * num2

    # Create the question and calculate answer
    question = f"{num1} {operator} {num2}"
    # eval() calculates string expressions
    answer = eval(question)

    return question, answer

def generate_basic_multiplication_problem():
    # Generate random numbers
    num1 = random.randint(0, 12)
    num2 = random.randint(0, 12)
    operator = '*'

    # Create the question and calculate answer
    question = f"{num1} {operator} {num2}"
    # eval() calculates string expressions
    answer = eval(question)

    return question, answer


# test question for add/sub
quest, ans = generate_basic_add_sub_problem()
user_answer = int(input(f"What is {quest}? "))

if user_answer == ans:
    print("Correct!")
else:
    print(f"Wrong. The answer is {ans}")


# test question for division
quest, ans = generate_basic_division_problem()
user_answer = int(input(f"What is {quest}? "))

if user_answer == ans:
    print("Correct!")
else:
    print(f"Wrong. The answer is {ans}")

# test question for multiplication
quest, ans = generate_basic_multiplication_problem()
user_answer = int(input(f"What is {quest}? "))

if user_answer == ans:
    print("Correct!")
else:
    print(f"Wrong. The answer is {ans}")