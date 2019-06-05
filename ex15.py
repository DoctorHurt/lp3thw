from sys import argv

if len(argv) != 2 :
    print(f"Usage: {argv[0]} <filename>")
    exit()

script, filename = argv

# txt will be the file object
txt = open(filename)

print(f"Here's your file {filename}:")
# We will now read the file object
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
