# This is the starting point of the program.
print("Hello World")  # Printing the classic "Hello World"
print("I was made in 2025")  # Telling the user when this code was created

# Asking the user for the current year.
print("What year is it?")
year = input()  # User input will be stored in the variable `year`
print("Wow, that's amazing!")

# Asking for the user's name and greeting them.
print("What is your name?")
name = input()  # Store the user's name in the variable `name`
print("Hello", name)

# Asking for the user's age and responding based on it.
print("What is your age?")
age = input()  # Store the user's age
print("Wow, you are", age)

# Ask about the user's life experience
print("How is life?")
life = input()  # User's response stored in `life`
if life == "good":
    print("That's good!")
else:
    print("Even though life is hard, try to be happy.")

# Asking about favorite color, food, etc.
print("What is your favorite color?")
color = input()  # User's favorite color stored here
print("That's a good color choice.")

print("What is your favorite food?")
food = input()  # Favorite food input
print("Delicious!")

print("What's 1 + 1?")
math = input()  # Simple math question
if math == "2":
    print("That's correct!")
else:
    print("That's incorrect, the answer is 2, but that's okay.")

# Continue asking about personal preferences
print("What's your favorite animal?")
animal = input()  # Favorite animal input
print("That's a good animal choice.")

print("What is your favorite sport?")
sport = input()  # Favorite sport input
print("That's a good sport choice.")

print("What's your favorite subject?")
subject = input()  # Favorite subject input
print("Knowing what subject you like is good because it can help you decide what you want to do in the future.")

# Ask about hobbies and drinks
print("What is your favorite hobby?")
hobby = input()  # User's favorite hobby
print("That's a good hobby.")

print("What is your favorite drink?")
drink = input()  # Favorite drink input
print("Yummy!")

# Asking about religion or an option to skip.
print("What's your religion or skip?")
religion = input()  # Store religion or skip
if religion.lower() == "skip":
    print("Okay.")
else:
    print("That's a good religion.")

# Asking for favorite movie, song, book, etc.
print("What is your favorite movie?")
movie = input()  # Favorite movie input
print("That's a good movie, all movies have something special.")

print("What is your favorite song?")
song = input()  # Favorite song input
print("That's an amazing song choice.")

print("What is your favorite book?")
book = input()  # Favorite book input
print(book, "is a good book.")

# Printing a statement about the program's purpose
print("This code was made to express your feelings; it doesn't mean anything.")

# Asking about favorite number and explaining the importance of numbers.
print("What is your favorite number?")
number = input()  # Favorite number input
print("Numbers make up everything, and you can learn a subject without knowing a little math.")
print("They're in history for dates like 2024, 1000, 2001.")
print("It's everywhere.")

# Simple login simulation
print("Here's a simple login page. The username is '1' and the password is '1'.")
print("Username")
username = input()  # Asking for the username
if username == "1":
    print("Password")
    password = input()  # Asking for the password
    if password == "1":
        print("Welcome!")
    else:
        print("Incorrect, but welcome!")
else:
    print("Incorrect, but welcome!")

# Explaining that this is a beginner's code
print("This code is long, but it's a good code for beginners.")
print("This code is made by a beginner.")

# A message for the user
print("I hope the future is good for you, and forever you care about", name)
print("Thank you for using this code.")

# Asking if the user wants to learn Python and providing a link
print("One more thing...")
print("Do you want to learn Python? (yes or no)")
ph = input().lower()  # Convert input to lowercase for easier comparison
if ph == "yes":
    print("https://www.youtube.com/watch?v=8KCuHHeC_M0")  # YouTube link for learning Python
    print("This will help you learn Python.")
elif ph == "no":
    print("Okay.")
else:
    print("Please respond with 'yes' or 'no'.")

# Ending message
print("Ok, Bye!")
print("This was made by codcodelan@gmail.com")  # Signature of the creator

# Tip for beginners: Always check the user's input carefully, especially when dealing with text inputs like names or numbers.
# You can also add more validation to handle unexpected inputs in a friendly way.
