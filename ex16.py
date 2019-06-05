from sys import argv
if len(argv) != 2 :
    print(f"Usage: {argv[0]} <filename>")
    exit()

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C NOW!")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Bye bye file!")
target.truncate()

print("Now Imma gonnna ask you for three lines of craptastic text.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Imma gonna write your craptastic lines to the file now, punk!")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we gonna close yo ungly azz file!")
target.close()
