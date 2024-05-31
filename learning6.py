#multiple condition statements
age1 = int(input("Please Type your age: \n"))

if age1 == 18 and age1 > 19 and age1 < 72:
    print("Target Range")
elif age1 == 19:
    print("Nineteen!!!!")
elif age1 < 18:
    print("Too young!")
else:
    print("Too old!")
    
    
    