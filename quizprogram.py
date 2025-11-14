# @author: PotionOfSweetness

import random
import time

# list of questions
question_bank = [
["What is Distance?\n A. Length travelled from first position to final position\n B. Total length travelled for a journey regardless of direction\n C. Total length of a journey including direction", "B"],
["What is Speed?\n A. How quickly an object is moving with no concern of direction\n B. How fast an object is moving with concern of direction\n C. Ratio of time divided by distance", "A"],
["What is Displacement?\n A. Straight distance and direction from initial point to final point\n B. The sum of initial position and final position\n C. The product of the intiial and final position with concern of direction", "A"],
["What is Kinematics?\n Fill in the blank. It is the study of ___", "MOTION"],
["Fill in the blank. A car's speedometer tells ___ speed.", "INSTANTANEOUS"],
["Fill in the blank. A car's odometer can allow us to find ___ speed.", "AVERAGE"],
["Fill in the blank. Speed, distance, time, are ___ quantities.", "SCALAR"],
["What is Scalar?\n A. Magnitude with no direction\n B. Magnitude with direction", "A"],
["What is Vector?\n A. Magnitude with no direction\n B. Magnitude with direction", "B"],
["What is acceleration due to gravity? (Hint: free fall)\n A. 9.7m/s\n B. 9.8m/s\n C. 9.9m/s\n D. 10.0m/s", "B"],
["When can the value of 'g' (acceleration due to gravity) not be used?\n A. Cannot be used at high altitudes\n B. Cannot be used on different planets\n C. A and B\n D. It can always be used", "C"],
["Fill in the blank. 'g' is true for an object with ___ and does not experience any ___ resistance. (Use a comma to separate individual answers).", "MASS, AIR"],
["If an object has constant velocity, what is it's acceleration?\n A. Acceleration will be the same as velocity\n B. We do know have enough information to find acceleration\n C. Acceleration will be 0.", "C"],
["If an object has constant speed, can it be accelerating?\n A. No, it cannot be accelerating.\n B. Yes, it can be accelerating.", "B"],
["Direction of acceleration is dependent on what?\n A. Whether an object speeds up or slows down\n B. Direction of velocity\n C. The opposite direction of velocity\n D. How the object feels emotionally during the interval", "A"],
["If an object speeds up, accceleration will be...\n A. the same as velocity\n B. the opposite of velocity", "A"],
["If an object slows up, accceleration will be...\n A. the same as velocity\n B. the opposite of velocity", "B"]
]

# color codes ansi color codes
# https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007
YELLOW = "\033[1;33m"
PINK = "\033[1;35m"
TEAL = "\033[1;36m"
WHITE = "\033[1;37m"

def run_menu():
    '''runs the menu '''
    
    # list of variables (the default option if the player doesnt change anything) - it will be set at the arguments of most functions later on
    name = "PLAYER"           
    number_of_questions = 5
    overcritical_mode_on = False
    program_running = True
    max_questions = len(question_bank)
    
    while program_running == True:  # loop menu unless they want to "quit"
        print(TEAL + "\n[ Menu ]" + WHITE)
        # menu options listed
        print("1. Settings")
        print("2. Play Quiz")
        print("3. Exit Program")
        
        menu_input = input("Enter a number: ")
        if menu_input == "1":
            # run settings with default options, then return the changes made and will set the new values to the variables
            name, number_of_questions, overcritical_mode_on, max_questions = run_settings(name, number_of_questions, overcritical_mode_on, max_questions)
        elif menu_input == "2":
            # run quiz with the needed arguments
            run_quiz(name, number_of_questions, overcritical_mode_on)
        elif menu_input == "3":
            print("* Exiting Program...")
            program_running = False
        else:
            print("* Invalid input. Try Again.\n")
            
def run_settings(name, number_of_questions, overcritical_mode_on, max_questions):
    ''' runs the settings '''
    valid_input = False     #input must be 1, 2, 3, or 4 (to select options)
    
    # settings options
    print(PINK + "\n[ Settings ]" + WHITE)
    print("1. Current Name:", name)
    print("2. Number of Questions:", number_of_questions)
    print("3. 'Overcritical Parent Mode' Activated:", overcritical_mode_on)
    print("4. Exit Settings")
    
    while valid_input == False:
        settings_input = input("Enter a number: ")
        
        if settings_input == "1":       #change name
            valid_input = True
            valid_name = False
            while valid_name == False:  #checks if input is alphabetical characters and checks for no spaces
                name = input("Enter Name: ").upper()
                if name.isalpha() and " " not in name:  # # https://www.w3schools.com/python/ref_string_isalpha.asp
                    valid_name = True
                    print("* Name has been updated to:", str(name) + ".")
                    return name, number_of_questions, overcritical_mode_on, max_questions
                else:
                    print("This is invalid input. Must only contain letters.")
                    
        elif settings_input == "2":    # change number of questions
            valid_input = True
            valid_number = False
            while valid_number == False:
                number_of_questions = input("Enter number of questions: ")
                try:
                    int(number_of_questions)    #tries to use the int() function to concatenate str to int
                except:
                    print("* This is invalid input.")   # if it fails to concatenate, it means the input contains characters that are not whole numbers
                else:                                   # if it does not fail, it will go on with the following code
                    if int(number_of_questions) >= 1 and int(number_of_questions) <= max_questions:     # checks if the input is less than 1 AND if it is less than the max_questions 
                        valid_number = True
                        print("* Number of Questions has been updated to:", str(number_of_questions) + ".")
                        return name, number_of_questions, overcritical_mode_on, max_questions           # returns values to settings function (where it was called), it will be in the loop because the menu is always looping
                    else:
                        if int(number_of_questions) < 1:
                            print("* The number of questions must be more than 0.")
                        else:
                            print("* This number exceeds the limit (MAX:", str(max_questions) + ").\n")
                            
        elif settings_input == "3":     # switch mode on / off
            valid_input = True
            overcritical_mode_on = not overcritical_mode_on
            print("* It has been switched to:", str(overcritical_mode_on) + ".")
            return name, number_of_questions, overcritical_mode_on, max_questions
        if settings_input == "4":   # exit settings
            print("* Exiting Settings...")
            return name, number_of_questions, overcritical_mode_on, max_questions #returns to menu (along with values, but the values did not change)
        else:
            print("* Invalid input. Try Again.\n")
            
def run_quiz(name, number_of_questions, overcritical_mode_on):
    ''' runs the quiz '''
    
    valid_input = False     #input must be 1 or 2 (to select options)
    print(YELLOW + "\n[ Quiz ]" + WHITE)
    
    # quiz options
    print("Welcome", name + ". There are", number_of_questions, "questions.")
    print("1. Generate Quiz")
    print("2. Exit Quiz")
    
    while valid_input == False:
        quiz_input = input("Enter a number: ")
        if quiz_input == "1":
            valid_input = True
            generate_quiz(name, number_of_questions, overcritical_mode_on)
            
        elif quiz_input == "2":
            valid_input = True
            print("* Exiting Quiz...")
            return name, number_of_questions, overcritical_mode_on
        
        else:
            print("* Invalid input. Try Again.\n")      

#generated responses to correct/incorrect inputs during the quiz
overcritical_parent_responses = ["Wrong!", "You're a failure!", "Awful.", "Terrible.", "Why did you think that was right?"]
nice_parent_responses = ["Nice try.", "Good effort!", "Aw man.", "Sorry, that's incorrect.", "It's okay, everyone makes mistakes."]

def generate_quiz(name, number_of_questions, overcritical_mode_on):
    ''' generates quiz questions + runs the actual quizzing system'''
    
    generated_list_of_questions = [ ]
    
    while len(generated_list_of_questions) < int(number_of_questions):  # loops until there are enough questions in the generated list (quiz) to meet the amount of questions the player preferred
        generated_question = random.choice(question_bank)               # selects a random question in the question bank
        if generated_question not in generated_list_of_questions:       # if its not already in the generated list (quiz), it will add it to it
            generated_list_of_questions.append(generated_question)      # this is done to not have repetitive questions
            
    print("\nGenerating...\n")
    time.sleep(1)   # waits 1 second, illusion of generating
    print(YELLOW + "[ The Quiz ]" + WHITE)
    
    number_of_correct_guesses = 0   # used to calculate score later on, makes note of how many they get correct
    question_number = 1             # number shown to indiciate to the player what number question they are answering
    
    i = 0  #i represents the index of the generated_list_of_questions
    while i < len(generated_list_of_questions):     # loops until it reaches the end, iterates thru each list element (question + answer)
        print(str(question_number) + ".", generated_list_of_questions[i][0])    #print the question number, then the first index of the element (first index is 0)
        question_number += 1
        guess = input("GUESS: ").upper()
        if guess == (generated_list_of_questions[i][1]):         # if the guess is equal to the answer (answer is stored in second index / index 1)
            print("Correct!\n")
            number_of_correct_guesses += 1                      # score goes up
        else:                                                   
            if overcritical_mode_on == True:
                print(random.choice(overcritical_parent_responses)) # runs the mean/nice response
            else:
                print(random.choice(nice_parent_responses))
            print("The answer was", (generated_list_of_questions[i][1]) + ".\n")    #tells player the right response if they were wrong
        i += 1
    calculate_score(number_of_correct_guesses, generated_list_of_questions, overcritical_mode_on) #calls calculate score function

def calculate_score(number_of_correct_guesses, generated_list_of_questions, overcritical_mode_on):
    ''' calculates score got from quiz + response'''
    score = str(number_of_correct_guesses) + "/" + str(len(generated_list_of_questions))    # states correct answers out of the total number of questions
    score_percetange = str(round(number_of_correct_guesses / len(generated_list_of_questions) *100, 2 ))    # formula to calculate percentage
    
    print(YELLOW + "SCORE:" + WHITE + score)
    print(YELLOW + "PERCENTAGE:" + WHITE, score_percetange + "%")
    
    # responses depending on your score
    if overcritical_mode_on == True:
        if float(score_percetange) == 100:
            print("Good job.")
        elif float(score_percetange) == 0:
            print("You're no son of mine.")
        elif float(score_percetange) >= 90 and float(score_percetange) != 100:
            print("Why didn't you get 100%?")
        elif float(score_percetange) >= 50:
            print("You only got", str(score_percetange) + "%? Try harder. You'll never be as good as your cousin.")
        elif float(score_percetange) < 50:
            print("You're going to end up homeless.")
        print("(¬_¬)")
    else:
        if float(score_percetange) == 100:
            print("Absolutely spectacular! I'm so proud of you.")
        elif float(score_percetange) >= 75 < 100:
            print("Amazing job!")
        elif float(score_percetange) >= 60:
            print("Keep up the good work! I believe in you!")
        elif float(score_percetange) < 60 and float(score_percetange) != 0:
            print("There's room for improvement, but good job! You tried your best!")
        elif float(score_percetange) == 0:
            print("You're worth isn't defined by a number. Keep working hard, you got this!")
        print("(>‿<) ♡")
    input("\n[ Click Enter to Continue ]")
    print("* Returning to Menu...")

def run_greeting_msg():
    ''' bella's kind message to new players + instructions'''
    print(TEAL + "[ Welcome to BELLA'S QUIZ PROGRAM! ]" + WHITE)
    print("* To navigate through the program, you can input numbers.")
    print("* Have fun! ('ᴗ')")

# runs the greeting_msg, then the menu that loops
run_greeting_msg()
run_menu()

# https://stackoverflow.com/questions/68655895/how-do-i-access-a-variable-that-is-inside-a-function-outside-the-function-in-pyt
# google ai overview
# chatgpt - helped with parameters + arguments, "/n", detected a duplicate in question bank
