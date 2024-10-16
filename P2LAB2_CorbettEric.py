#Eric Corbett
#10/5/2024
#Using dictionaries
#P2LAB2

cars = {'camero':18.21, 'prius':52.36, 'model S':110, 'silverado':26}


#get keys from dict
cars_keys = cars.keys()

print(cars_keys)
print(*cars_keys, sep = ",")

#Get a car from user
car_name = input("Enter a car:")

#get mpg for the given
car_mpg = cars[car_name]
print(f"the {car_name} get {car_mpg} miles per gallon")

#Get miles from user
miles_driven =float(input(f"How many miles will you drive the {car_name}?"))

#calculate
gallons_needed = miles_driven/car_mpg

                          
#display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name}{miles_driven} miles")                          
