apples = input("How many apples did you eat?")
if apples:
    apples = int(apples)
    if apples == 0:
        print("An apple a day keeps the doctor away. Eat an apple, please")
    elif apples <= 3:
        print("Good job")
    elif apples <= 6:
        print("That is a lot of apples")
    elif apples <= 10:
        print("ehm")
    else:
        print("Are you crazy?")
else:
    print("Please enter a number")
