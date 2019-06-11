people = 30
cars = 40
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("Not enough cars, take a walk instead.")
else:
    print("We can't decide to take a car or walk.")

if trucks > cars:
    print("Too many trucks!")
elif trucks < cars:
    print("Maybe we could take the trucks even tho there is not enough.")
else:
    print("We still can't decide on trucks.")

if people > trucks:
    print("Alright, let's just take trucks since there are so many.")
else:
    print("Fine, lets just stay home and play video games instead.")
