# U.S. President Knowledge Quiz
# This program quizzes the user on U.S. Presidents and provides a score at the end. 
score = 0

print("Welcome to the U.S. President Knowledge Quiz!")

# Question 1
answer1 = input("1. Who was the first president of the United States?\n(a) George Washington\n(b) Abraham Lincoln\n(c) Thomas Jefferson\n(d) John Adams\nEnter your answer: ")
while answer1 not in ["a", "b", "c", "d"]: # Check if the user's input is valid and it will keep running util the user enters a valid input
    print("Invalid response. Please enter a, b, c, or d.")
    answer1 = input("Enter your answer: ") # Ask the user to enter their answer again
if answer1 == "a": # Check if the user's answer is correct
    print("Correct!")
    score += 1 # Add 1 to the score if the user's answer is correct
else:
    print("Wrong! The correct answer is George Washington.")    

# Question 2
answer2 = input("2. Which President issued the Emancipation Proclamation?\n(a) Abraham Lincoln\n(b) Thomas Jefferson\n(c) George Washington\n(d) John Adams\nEnter your answer: ")
while answer2 not in ["a", "b", "c", "d"]: # Check if the user's input is valid and it will keep running util the user enters a valid input
    print("Invalid response. Please enter a, b, c, or d.")
    answer2 = input("Enter your answer: ") # Ask the user to enter their answer again
if answer2 == "a": # Check if the user's answer is correct
    print("Correct!")
    score += 1 # Add 1 to the score if the user's answer is correct
else:
    print("Wrong! The correct answer is Abraham Lincoln.")

# Question 3 
answer3 = input("3. Who was the only U.S. President to serve more than two terms?\n(a) George Washington\n(b) Thomas Jefferson\n(c) Franklin D. Roosevelt\n(d) John Adams\nEnter your answer: ")
while answer3 not in ["a", "b", "c", "d"]: # Check if the user's input is valid and it will keep running util the user enters a valid input
    print("Invalid response. Please enter a, b, c, or d.")
    answer3 = input("Enter your answer: ") # Ask the user to enter their answer again
if answer3 == "c": # Check if the user's answer is correct
    print("Correct!")
    score += 1 # Add 1 to the score if the user's answer is correct
else:
    print("Wrong! The correct answer is Franklin D. Roosevelt.")

# Question 4
answer4 = input("4. Which U.S. President resigned from office?\n(a) George Washington\n(b) Thomas Jefferson\n(c) Richard Nixon\n(d) John Adams\nEnter your answer: ")
while answer4 not in ["a", "b", "c", "d"]: # Check if the user's input is valid and it will keep running util the user enters a valid input
    print("Invalid response. Please enter a, b, c, or d.")
    answer4 = input("Enter your answer: ") # Ask the user to enter their answer again
if answer4 == "c": # Check if the user's answer is correct
    print("Correct!")
    score += 1 # Add 1 to the score if the user's answer is correct
else:
    print("Wrong! The correct answer is Richard Nixon.")

# Question 5
answer5 = input("5. Who was the youngest elected U.S. President?\n(a) John F. Kennedy\n(b) Theodore Roosevelt\n(c) Barack Obama\n(d) Bill Clinton\nEnter your answer: ")
while answer5 not in ["a", "b", "c", "d"]: # Check if the user's input is valid and it will keep running util the user enters a valid input
    print("Invalid response. Please enter a, b, c, or d.") 
    answer5 = input("Enter your answer: ") # Ask the user to enter their answer again
if answer5 == "a": # Check if the user's answer is correct
    print("Correct!")
    score += 1 # Add 1 to the score if the user's answer is correct
else:
    print("Wrong! The correct answer is John F. Kennedy.")

# Display Results
print("\nQuiz Complete!")

if score == 5:
    print("Congratulations! You got a perfect score of 5/5!")
elif score == 4:
    print("Good job! You got 4/5.")
elif score == 3:
    print("Not bad! You got 3/5.")
elif score == 2:
    print("You got 2/5. Keep practicing!")    
elif score == 1:
    print("You got 1/5. Keep practicing!")
else:    
    print("You got 0/5. Better luck next time!")
