print("Welcome to iChat Chatbox!")
user_name = input("Before we get started, what is your name?")
print(f'Hello {user_name}! ')
user_age = input("What is your age?")
print("That's great!")
print(f'How may I assist you {user_name}?')


def chat_functions():
  print("-- 1. Placeholder (Write a passage) --")
  print("-- 2. Placeholder (Answer questions) --")
  print("-- 3. Placeholder (Describe in detail) --")
  print("-- 4. Placeholder (Have a Conversation) --")
  print("-- 5. Exit Chat --")
  

chat_functions()
user_choice = input("What would you like to do?(input a number 1-5)")

if user_choice == "1":
   print("Placeholder 1 !")
if user_choice == "2":
   print("Placeholder 2 !")
if user_choice == "3":
   print("Placeholder 3 !")
if user_choice == "4":
   print("Placeholder 4 !")
if user_choice == "5":
  print("Thank you for using iChat Chatbox!")
  print("Exiting Chatbox...")
  quit()     

  
# The only source that I used as reference for this assignment 
# was my previous coding projects done in Wave 1 for Software Development.