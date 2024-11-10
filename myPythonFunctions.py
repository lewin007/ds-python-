# myPythonFunctions.py

import random
import os

# Task 2: Get user score
def getUserPoint(userName):
    try:
        with open('userScores.txt', 'r') as file:
            for line in file:
                data = line.strip().split(', ')
                if data[0] == userName:
                    return int(data[1])
        return -1
    except FileNotFoundError:
        return -1

# Task 3: Update user points
def updateUserPoints(newUser, userName, score):
    if newUser:
        with open('userScores.txt', 'a') as file:
            file.write(f"{userName}, {score}\n")
    else:
        with open('userScores.txt', 'r') as file:
            lines = file.readlines()
        
        with open('userScores.tmp', 'w') as temp_file:
            for line in lines:
                data = line.strip().split(', ')
                if data[0] == userName:
                    temp_file.write(f"{userName}, {score}\n")
                else:
                    temp_file.write(line)
        
        os.remove('userScores.txt')
        os.rename('userScores.tmp', 'userScores.txt')

# Task 4: Generate arithmetic questions
def generateQuestion():
    operandList = [0] * 5
    operatorList = [""] * 4
    operatorDict = {1: '+', 2: '-', 3: '*', 4: '**'}

    # Action 4.1: Update operandList with random numbers
    for i in range(len(operandList)):
        operandList[i] = random.randint(1, 10)

    # Action 4.2: Update operatorList with random math symbols, ensuring no consecutive '**'
    for i in range(len(operatorList)):
        while True:
            operator = operatorDict[random.randint(1, 4)]
            if not (operator == '**' and operatorList[i - 1] == '**'):
                operatorList[i] = operator
                break

    # Action 4.3: Generate a mathematical expression as a string
    questionString = f"{operandList[0]}"
    for i in range(4):
        questionString += f" {operatorList[i]} {operandList[i + 1]}"
    
    # Action 4.4: Evaluate the result of the question
    result = eval(questionString)

    # Replace '**' with '^' for display purposes
    displayString = questionString.replace("**", "^")
    
    return displayString, result

# Task 4.5: Interact with the user
def askQuestion():
    question, answer = generateQuestion()
    print(f"Question: {question}")
    
    while True:
        user_input = input("Your answer (or -1 to quit): ")
        if user_input == "-1":
            return -1
        try:
            user_answer = int(user_input)
            if user_answer == answer:
                print("Correct!")
                return 1
            else:
                print(f"Incorrect. The correct answer is {answer}.")
                return 0
        except ValueError:
            print("Invalid input. Please enter a number.")
