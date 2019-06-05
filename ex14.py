from sys import argv

if len(argv) != 2 :
    print("Please supply your username as the first argument to this script, yo.")
    exit()

script, user_name = argv
prompt = '=> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print("Where do you live?")
lives = input(prompt)

print("What kind of compuper do you have?")
compuper = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {compuper} compuper. Not very nice.
""")
