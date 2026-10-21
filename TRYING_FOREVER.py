#======================== Trying Forever ============================
print("======================== Trying Forever ============================")
print("Welcome to Trying forever")
print()

valid=False
while not valid:
    try:
        WOFisBest= int(input("enter a number: "))

        while WOFisBest%2 == 0:
            print("WOF IS BEST AND I LOVE BEST AND MOONWATCHER IS MY OG!")
        valid=True
    except ValueError as Moonwatcher:
        print("IVALID INPUT!")