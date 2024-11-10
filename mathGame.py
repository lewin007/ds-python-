# mathGame.py

import myPythonFunctions

def main():
    try:
        # Get the user's name and score
        userName = input("Enter your name: ")
        userScore = myPythonFunctions.getUserPoint(userName)
        newUser = userScore == -1
        if newUser:
            userScore = 0

        print(f"Welcome, {userName}! Your current score is {userScore}.")

        # Main game loop
        while True:
            userChoice = myPythonFunctions.askQuestion()
            if userChoice == -1:
                break
            userScore += userChoice
            print(f"Your updated score is {userScore}.")

        # Update user's score on exit
        myPythonFunctions.updateUserPoints(newUser, userName, userScore)
        print("Thanks for playing!")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
