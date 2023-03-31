age = int(input("What is your age?"))
drinks = ['Hennessy',
           'Gulder',
           'Fearless',
           'Star',
           'Heineken',
           'Fanta',
           'Coca Cola',
           'Sprite',
           'Fruit Juice',
           'Tea',
           'Coffee']

if age < 18:
    print("you are too young to buy beer")
    print("This are the drinks for you")
    for drink in drinks[5:]:
        print(drink)
elif 18 <= age <= 50:
    print("Which bear do you want")
    for d in drinks:
        print(d)
else:
    print("You're too old try coffee")


name = input("What is you name?")
if name == "kezi":
    print("Eureka")
else:
    name = input("Who are u")
    if len(name) > 10:
        x = 1
        while x > 0:
            print(1)
            x += 1
