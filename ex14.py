from sys import argv

script, user_name, thoughts = argv
something_else = 'AA'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(something_else)

print(f"What do you think?")
lives = input(thoughts)

print(f"Where do you live {user_name}?")
lives = input(something_else)

print("What kind of computer do you have?")
computer = input(something_else)

print(f"""
        Alright, so you said {likes} about liking me.
        You live in {lives}. Not sure where that is.
        And you have a {computer} computer. Nice.
        """)
