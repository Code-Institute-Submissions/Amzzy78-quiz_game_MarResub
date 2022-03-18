import sys
print("Welcome to Irish Folklore Quiz!")
# ---------------------------------------

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1
 
# Nested for loop
    for key in questions:
        print("-----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        # User input and prompt.
        guess = input("Enter (A, B, C, D):\n ")
        guess = guess.upper()
        guesses.append(guess)
        # Fill in the check_answer function and pass the key for current
        # question and guess function.
        correct_guesses += check_answer(questions.get(key), guess)
        # Increment each question number after each iteration.
        question_num += 1


# Display the final score outside the for loop.
    display_score(correct_guesses, guesses)     

# Set up parameters for the check_answer function         
# ---------------------------------


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# ---------------------------------


def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")
    print("-----------------------------")

    print("Answers: ", end="")
    # Display questions loop
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    # Display guesses loop
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions)) * 100)
    print("Your score is: "+str(score)+"%")
# ---------------------------------


# def play_again():

#     response = input("Do you want to play again? (yes or no): ")
#     response = response.upper()

#     if response == "Yes":
#         play_again()
#     else:
#         if response == "No":
    
#             print("Bye! ")
       
def play_again():
    """Returns True or False"""
    while True:
        # As a convention the capital Y indicates that 
        # hitting enter without any input means yes; yes is default.
        answer = input("Do you want to play again? (Y/n): ")
        if not answer or answer.lower() in ('y', 'yes'):
            return True
        elif answer.lower() in ('n', 'no'):
            return False
        else:
            print("Not a valid answer!")       


# ---------------------------------
# Create dictionary for questions

questions = {
    "Who trained for 20 years in subjects such as law, astronomy, philosophy, poetry, medicine, music, geometry divination, and magic?: ": "A",
    "What is a common ancient Irish beverage used also for ritual where it would be spiked with certain herbs ?: ": "B",
    "In Irish Folklore what was eaten eaten by the Salmon, fished up by the druid, and cooked by young Finn, who, as sorcerer’s apprentice, burns his thumb on the Salmon’s skin, sticks thumb in mouth, and attains all the wisdom in his master’s stead?: ": "C",
    "In Irish Mythology what is the name of the story of the son of a warrior chieftain, who experiences an ‘Isle of intoxicating wine fruits’ during his journey to avenge his father’s death?: ": "A",
}

# Create a list of lists to hold the answers and responds to a key value pair 
# within the list of questions


options = [["A. Druids", "B. Fionn mac Cumhaill", "C. Michael D Higgins", "D. Biddy Early"],
    ["A. Poitin", "B. Mead", "C. Guinness", "D. Whiskey"],
    ["A. Algae", "B. Seaweed", "C. Hazelnuts", "D. Potatoes"],
    ["A. The Voyage of Máel Dúin", "B. Tír na nÓg", "C. The Children of Lir", "D. Táin Bó Cúailnge"]]

# Call the new_game function to begin a new game

def main():
    while True:
        new_game()
        if not play_again():
            return


if __name__ == '__main__':
    main()
    print("Bye! ")
    sys.exit()





