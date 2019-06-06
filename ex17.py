from sys import argv
from os.path import exists

if len(argv) != 3 :
    print(f"Usage: {argv[0]} <from-file> <to-file>")
    exit()

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abortz.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done yo!")

out_file.close()
in_file.close()
