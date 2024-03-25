
def enum(**enums):
    return type('Enum', (), enums)

Choice = enum(Easy=1, Medium=2, Hard=3)
choice = int(input("Enter choice: "))

print(Choice.Easy)

if choice == Choice.Easy:
    print("You chose the easy option")
elif choice == Choice.Medium:
    print("You chose the medium option")
elif choice == Choice.Hard:
    print("You chose the hard option")
else:
    print("You should choose one of the three levels!")
