import json

questions = [
  "Rate 'Pictionary' on a scale of 1 to 5",
  "Rate 'Kunja' on a scale of 1 to 5",
  "Rate 'Mafia' on a scale of 1 to 5",
  "Rate 'This is a pen' on a scale of 1 to 5",
  "Rate 'Human tic tac toe' on a scale of 1 to 5",
  "Rate 'Ninja' on a scale of 1 to 5",
  "Rate 'Traffic Jam' on a scale of 1 to 5",
  "Rate 'Come to my party' on a scale of 1 to 5",
  "Rate 'Telephone' on a scale of 1 to 5",
  "Rate 'Bang' on a scale of 1 to 5",
  "Rate 'Human Knot' on a scale of 1 to 5",
  "Rate 'Telepathic Counting' on a scale of 1 to 5",
  "Rate 'Secret Dancer' on a scale of 1 to 5",
  "Rate 'Four Corners' on a scale of 1 to 5"
]

keys = ["Pictionary", "Kunja", "Mafia", "This is a pen", "Human tic tac toe", "Ninja", "Traffic Jam", "Come to my party", "Telephone", "Bang", "Human Knot", "Telepathic Counting", "Secret Dancer", "Four Corners"]

listAnswers = []

done = "no"

while done :
    answers = {}

    print("   ")
    print("   ")
    print("   ")
    print("   ")
    print("This is a new Survey! Please respond to the following questions: ")
    print("   ")

    for x in range(len(questions)):
        response = input(questions[x] + " ")
        answers[keys[x]] = response

    listAnswers.append(answers)

    done = input("Are you the last person taking this survey? Yes or No?").lower()
    if input == "yes" or "Yes" :
        print(answers)
        exit()

print(answers)

f = open("mySurvey.json", "a")
f.write('[\n')
index = 0
for t in listAnswers:
    if (index < len(listAnswers)-1):
        json.dump(t, f)
        f.write(',\n')
    else:
        json.dump(t,f)
        f.write('\n')
    index += 1

f.write(']')
f.close()
