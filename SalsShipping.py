print("Welcome to Sal's Shipping!")

def get_package_weight():
    while True:
        try:
            weight_lbs = float(input("Please enter the weight of your package in pounds: "))
            return weight_lbs
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    package_weight = get_package_weight()
    print(f"Package weight: {package_weight} lbs")

#Defining Variables
groundShipping = 00.00
droneShipping = 00.00
goundPremium = 125.00

#Calculating Costs
if package_weight <= 2.00:
    groundShipping = (package_weight * 1.50) + 20.00
    droneShipping = package_weight * 4.50

elif package_weight > 2.00 and package_weight <= 6.00:
    groundShipping = (package_weight * 3.00) + 20.00
    droneShipping = package_weight * 9.00

elif package_weight > 6.00 and package_weight <= 10.00:
    groundShipping = (package_weight * 4.00) + 20.00
    droneShipping = package_weight * 12.00

elif package_weight > 10.00:
    groundShipping = (package_weight * 4.75) + 20.00
    droneShipping = package_weight * 14.25

else:
    print("Something has gone wrong lol")

#Print all shipping method cost totals:
print(f"Gound Shipping Cost:     $ {groundShipping}")
print(f"Drone Shipping Cost:     $ {droneShipping}")
print(f"Premium Ground Shipping: $ {goundPremium}")

#What is cheapest method for customer to deliver?
cheapest_method = min(groundShipping, droneShipping, goundPremium)
if cheapest_method == groundShipping:
    recommended_method  =  "Ground Shipping"
elif cheapest_method  ==  droneShipping:
    recommended_method  = "Drone Shipping"
elif cheapest_method  ==  goundPremium:
    recommended_method = "Premium Ground Shipping"

print(f"The Cheapest Method: {recommended_method}")