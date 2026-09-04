import random

#variables
rider_choice = "guerrila 450"
cc = 450
bhp = 50

print(rider_choice)
print(cc)


#functions
def get_rider():
    
    # bike = input("Enter your bike name: ")
    cc = 450
    bhp = 40
    nm = 40

    #lists
    listOfBikes = ["guerrila 450", "duke 390", "speed 400"]
    bike = random.choice(listOfBikes)

    #dictionary to store the variables
    dic_var = {
        "bike" : bike,
        "cc" : cc,
        "bhp" : bhp,
        "nm" : nm

    }
    return dic_var
response = get_rider()


# print(response)

age = input("Enter your age: ")

if int(age) < 18:
    print(f"You are not eligible to ride a bike because your age is {age}")
elif int(age) > 100:
    print(f"You are not eligible to ride a bike because your age is {age}")
else:
    print(f"You are eligible to ride a bike because your age is {age}")