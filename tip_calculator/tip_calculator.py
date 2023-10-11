#Gather Information from User
print("Welcome to the 'Tip Calculator'")
amount = float(input("Please enter the total of the bill: "))
tip = int(input("What percentage tip would you like to leave(10, 12, 15)? "))
num_people_paying = int(input("How many people to split the bill: "))

#Add tip to total
total = amount + ((tip / 100) * amount)

#Divide by number of people paying and round the number
grand_total = round(total / num_people_paying, 2)

#print tip amount
print(f"Each person should pay: ${grand_total:.2f}")


