print("Enter total numbers: ")
tn = int(input("> "))
print("Enter increment value: ")
iv = int(input("> "))

numbers = list()

def listAppend(totalnums, incr=1):
    """ Appends totalnums numbers to the end of the numbers list
    using incr increment """
    for i in range(tn):
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + incr
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

listAppend(tn, iv)

print("The numbers: ")
for num in numbers:
    print(num)
