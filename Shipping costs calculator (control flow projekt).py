################################
#SELECT INPUT#

print("##### PICKLES' SHIPPING PRICE CALCULATOR #####")
print(" ")

#Type in shipping type:
#selected_flat_charge_rate = 2
#Type in weight of package:
#weight_of_package = 41.5
weight_of_package = float(input("Please exact weight (format xx.xx):  "))

print("")
print("You have selected: ")
print("Weight: " + str(weight_of_package) + " lbs")

print(" ")
print(" ")
print("Ground shipping flatrate $20.00 (type 1)")
print("Drone shipping flatrate $0.00 (type 2)")
print("Premium shipping flatrate $125.00 (type 3)")

selected_flat_charge_rate = int(input("Please enter shipping type 1, 2 or 3:  "))

if selected_flat_charge_rate == 1:
  print("Shipping type: " + str(selected_flat_charge_rate) + " (ground shipping)")
elif selected_flat_charge_rate == 2:
  print("Shipping type: " + str(selected_flat_charge_rate) + " (drone shipping)")
elif selected_flat_charge_rate == 3:
  print("Shipping type: " + str(selected_flat_charge_rate) + " (premium shipping)")

print(" ")
print("#################")
################################

#FLATCHARGE RATES
ground_shipping_fc = 20
drone_shipping_fc = 0
premium_shipping_fc = 125

################################
#SELECT FLATCHARGE RATE#

print(" ")

if selected_flat_charge_rate == 1:
  print("Your selected shipping: Ground shipping")
elif selected_flat_charge_rate == 2:
  print("Your selected shipping: Drone shipping")
elif selected_flat_charge_rate == 3:
  print("Your selected shipping: is Premium shipping")
else:
  print("Please make sure to select a shipping method")

################################
#PACKAGE TYPE

def flat_charge_rate(package_type):
  if package_type == 1: 
    global flatcharge_1
    flatcharge_1 = ground_shipping_fc
    return flatcharge_1
  elif package_type == 2:
    global flatcharge_2
    flatcharge_2 = drone_shipping_fc
    return flatcharge_2
  elif package_type == 3:
    global flatcharge_3
    flatcharge_3 = premium_shipping_fc
    return flatcharge_3
  elif package_type == 0 or package_type > 3:
    print("Invalid package type")

print("Flat charge rate is " + str(flat_charge_rate(selected_flat_charge_rate)) + "$")

################################
#WEIGHT

#Prices - Ground shipping
#2 lb or less
gs_2 = 1.50
#Over 2 but less than or equal to 6 lb
gs_2_to_6 = 3
#Over 6 but less than or equal to 10 lb
gs_6_to_10 = 4
#Over 10
gs_10 = 4.75

#Prices - Drone shipping
#2 lb or less
ds_2 = 4.5
#Over 2 but less than or equal to 6 lb
ds_2_to_6 = 9
#Over 6 but less than or equal to 10 lb
ds_6_to_10 = 12
#Over 10
ds_10 = 14.25

def weight_charge_rate(package_weight):
  if selected_flat_charge_rate == 1 and package_weight <= 2:
    return (gs_2 * package_weight) + flatcharge_1
  elif selected_flat_charge_rate == 1 and package_weight > 2 and package_weight <= 6:
    return (gs_2_to_6 * package_weight) + flatcharge_1
  elif selected_flat_charge_rate == 1 and package_weight > 6 and package_weight <= 10:
    return (gs_6_to_10 * package_weight) + flatcharge_1
  elif selected_flat_charge_rate == 1 and package_weight > 10:
    return (gs_10 * package_weight) + flatcharge_1
  elif selected_flat_charge_rate == 2 and package_weight <= 2:
    return (ds_2 * package_weight) + flatcharge_2
  elif selected_flat_charge_rate == 2 and package_weight > 2 and package_weight <= 6:
    return (ds_2_to_6 * package_weight) + flatcharge_2
  elif selected_flat_charge_rate == 2 and package_weight > 6 and package_weight <= 10:
    return (ds_6_to_10 * package_weight) + flatcharge_2
  elif selected_flat_charge_rate == 2 and package_weight > 10:
    return (ds_10 * package_weight) + flatcharge_2
  elif selected_flat_charge_rate == 3:
    return 125
  else:
    return "ERROR: Total cannot be calculated, please make sure to type in weight and shipping type"

print("*********************")
print("Your total is: " + str(weight_charge_rate(weight_of_package)) + "$")
print("*********************")

################################
#COMPARE PRICES

print(" ")

def weight_costs_droneshipping(package_weight):
  if package_weight <= 2:
    return (ds_2 * package_weight) + 0
  elif package_weight > 2 and package_weight <= 6:
    return (ds_2_to_6 * package_weight) + 0
  elif package_weight > 6 and package_weight <= 10:
    return (ds_6_to_10 * package_weight) + 0
  elif package_weight > 10:
    return (ds_10 * package_weight) + 0

def weight_costs_groundshipping(package_weight):
  if package_weight <= 2:
    return (gs_2 * package_weight) + 20
  elif package_weight > 2 and package_weight <= 6:
    return (gs_2_to_6 * package_weight) + 20
  elif package_weight > 6 and package_weight <= 10:
    return (gs_6_to_10 * package_weight) + 20
  elif package_weight > 10:
    return (gs_10 * package_weight) + 20

if weight_costs_droneshipping(weight_of_package) > weight_costs_groundshipping(weight_of_package) and selected_flat_charge_rate == 2 and weight_costs_droneshipping(weight_of_package) < 125 and weight_costs_groundshipping(weight_of_package) < 125:
  print("Did you know: Ground shipping is actually cheaper with that amount of weight:")
  print("Ground shipping costs: " + str(weight_costs_groundshipping(weight_of_package)) + " $")
  print("Drone shipping costs: " + str(weight_costs_droneshipping(weight_of_package)) + " $")
elif weight_costs_droneshipping(weight_of_package) < weight_costs_groundshipping(weight_of_package) and selected_flat_charge_rate == 1 and weight_costs_droneshipping(weight_of_package) < 125 and weight_costs_groundshipping(weight_of_package) < 125:
  print("Did you know: Drone shipping is actually cheaper with that amount of weight:")
  print("Ground shipping costs: " + str(weight_costs_groundshipping(weight_of_package)) + " $")
  print("Drone shipping costs: " + str(weight_costs_droneshipping(weight_of_package)) + " $")
elif weight_costs_droneshipping(weight_of_package) == weight_costs_groundshipping(weight_of_package):
  print("Both methods have the same prices")
elif weight_charge_rate(weight_of_package) > 125:
  print("Did you know: Premium shipping is actually cheaper with that amount of weight:")
  print("Premium shipping costs: 125$")


