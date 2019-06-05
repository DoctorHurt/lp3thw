from sys import argv
# read the WYSS section for how to run this
if len(argv) != 4 :
    print("Wrong number of vars. We need three.")
    exit()

script, first, second, third = argv

print("The script is called:", script)
print("Your first var is:", first)
print("Your second var is:", second)
print("Your third var is:", third)
