
# Creates the dictionary to store responses.

'''
Below, write code that will pose the survey questions from the student prompt
to a user. Your program should save user input as a dictionary.
'''

games = {

    'Pictionary': '',
    'Kunja': '',
    'Mafia': '',
    'This is a pen': '',
    'Human tic tac toe': '',
    'Ninja': '',
    'Traffic Jam': '',
    'Come to my party': '',
    'Telephone': '',
    'Bang': '',
    'Human Knot': '',
    'Telepathic Counting': '',
    'Secret Dancer': ''
}

users = {}

# Displays option: Game
# Rate thsi from a scale of 1 - 10
# Add information to the dictionary

while True:
    print("Rate this game on a scale of 1 to 5 : Pictionary : ")
    userInput1 = input()
    if userInput1 == "1" or "2" or "3" or "4" or "5":
        print("Thank you for rating this game.")
        print(" ")
        games['Pictionary'] = userInput1

        print("Rate this game on a scale of 1 to 5 : Kunja : ")
        userInput1 = input()
        if userInput1 == "1" or "2" or "3" or "4" or "5":
            print("Thank you for rating this game.")
            print(" ")
            games['Kunja'] = userInput1

            print("Rate this game on a scale of 1 to 5 : Mafia : ")
            userInput1 = input()
            if userInput1 == "1" or "2" or "3" or "4" or "5":
                print("Thank you for rating this game.")
                print(" ")
                games['Mafia'] = userInput1

                print("Rate this game on a scale of 1 to 5 : This is a pen : ")
                userInput1 = input()
                if userInput1 == "1" or "2" or "3" or "4" or "5":
                    print("Thank you for rating this game.")
                    print(" ")
                    games['This is a pen'] = userInput1

                    print("Rate this game on a scale of 1 to 5 : Human Tic Tac Toe : ")
                    userInput1 = input()
                    if userInput1 == "1" or "2" or "3" or "4" or "5":
                        print("Thank you for rating this game.")
                        print(" ")
                        games['Human Tic Tac Toe'] = userInput1

                        print("Rate this game on a scale of 1 to 5 : Ninja : ")
                        userInput1 = input()
                        if userInput1 == "1" or "2" or "3" or "4" or "5":
                            print("Thank you for rating this game.")
                            print(" ")
                            games['Ninja'] = userInput1

                            print("Rate this game on a scale of 1 to 5 : Traffic Jam : ")
                            userInput1 = input()
                            if userInput1 == "1" or "2" or "3" or "4" or "5":
                                print("Thank you for rating this game.")
                                print(" ")
                                games['Traffic Jam'] = userInput1

                                print("Rate this game on a scale of 1 to 5 : Come to my Party : ")
                                userInput1 = input()
                                if userInput1 == "1" or "2" or "3" or "4" or "5":
                                    print("Thank you for rating this game.")
                                    print(" ")
                                    games['Come to my Party'] = userInput1

                                    print("Rate this game on a scale of 1 to 5 : Telephone : ")
                                    userInput1 = input()
                                    if userInput1 == "1" or "2" or "3" or "4" or "5":
                                        print("Thank you for rating this game.")
                                        print(" ")
                                        games['Telephone'] = userInput1

                                        print("Rate this game on a scale of 1 to 5 : Bang : ")
                                        userInput1 = input()
                                        if userInput1 == "1" or "2" or "3" or "4" or "5":
                                            print("Thank you for rating this game.")
                                            print(" ")
                                            games['Bang'] = userInput1

                                            print("Rate this game on a scale of 1 to 5 : Human Knot : ")
                                            userInput1 = input()
                                            if userInput1 == "1" or "2" or "3" or "4" or "5":
                                                print("Thank you for rating this game.")
                                                print(" ")
                                                games['Human Knot'] = userInput1

                                                print("Rate this game on a scale of 1 to 5 : Telepathic Counting : ")
                                                userInput1 = input()
                                                if userInput1 == "1" or "2" or "3" or "4" or "5":
                                                    print("Thank you for rating this game.")
                                                    print(" ")
                                                    games['Telepathic Counting'] = userInput1

                                                    print("Rate this game on a scale of 1 to 5 : Secret Dancer : ")
                                                    userInput1 = input()
                                                    if userInput1 == "1" or "2" or "3" or "4" or "5":
                                                        print("Thank you for rating this game.")
                                                        print(" ")
                                                        games['Secret Dancer'] = userInput1
                                                        print(games)
                                                        exit()


# Print the context of the dictionary.
#print(answers)
