#Eligiblity checker for car rental service.
age=int(input("Enter your age: "))
if age>=21:
    license=input("Do you have a license? ") 
    if license == "yes": #all letters are must be small letter.
        print("You are Eligiable to car rental.") 
    else:
        print("You are not eligiable for car rental")
else:
    print("You are not Eligiable for car rental.")
