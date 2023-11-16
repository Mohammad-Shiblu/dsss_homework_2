import random
def num_generator(min, max):
    """
    Return a Random integer between min and max.
    Args:
        min(int): Minimum integer to choose
        max(int): Maximum integer to choose
    Return:
        int: Randomly selected integer between min and max
    """
    return random.randint(min, max)     # Generate random integer between min and max
def operation_selection():
    """
    Return a Randomly selected operation.
    Return:
        string: Randomly selected operation symbol
    """
    return random.choice(['+', '-', '*'])   # randomly choose operation

def math_operation(num1, num2, op):
    """
    Perform a selected mathematical operation
    Args:
        num1(float): a floating number for operation
        num2(float): a floating number for operation
        op(string): Operation selector
    Return:
        pb(string): string showing the operand
        result (float): Result after the operation
    """
    pb = f"{num1} {op} {num2}"
    if op == '+':                # perform add operation
        result = num1 + num2
    elif op == '-':              # perform subtraction
        result = num1 - num2
    else:                       # perform multiplication
        result = num1 * num2
    return pb, result

def math_quiz():
    """
    perform the quiz operation as main function. collect user answer and track the score.
    """
    points = 0
    turns = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(turns):                          # Loop through for the number of turns
        num1 = num_generator(1, 10)
        num2 = num_generator(1, 8)
        op = operation_selection()

        PROBLEM, ANSWER = math_operation(num1, num2, op)
        print(f"\nQuestion: {PROBLEM}")
        while True:
            try:                                     # to handle invalid input error from the user
                useranswer = input("Your answer: ")  # receive user answer
                useranswer = int(useranswer)
                break  # Break out of the loop if the input is successfully converted to an integer
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        if useranswer == ANSWER:                    # Check user answer if it is correct
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{turns}")

if __name__ == "__main__":
    math_quiz()
