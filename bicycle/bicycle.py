from classes import *
import random

debug = False
    
""" Wheels"""
wheels = [Wheel(4, 55, 'W1'), 
          Wheel(5, 35, 'W2'), 
          Wheel(6, 15, 'W3')]
if debug:   
    for i in wheels: i.describe()

""" Frames """ 
frames = [Frame(4,  600, 'Carbon'),    # 0
          Frame(5,  500, 'Carbon'),    # 1
          Frame(6,  400, 'Aluminum'),  # 2
          Frame(7,  300, 'Aluminum'),  # 3
          Frame(8,  200, 'Steel'),     # 4
          Frame(9,  100, 'Steel'),     # 5
          Frame(10, 50, 'Steel')]     # 6
if debug: 
    for i in frames: i.describe()

""" Manufacturers """
manufacturers = [Manufacturer('A', [], 15), 
                 Manufacturer('B', [],  5), 
                 Manufacturer('C', [], 25)]

""" Models """
models = [Model(wheels[0], frames[0],  "M1", manufacturers[0]), # 0
          Model(wheels[0], frames[1],  "M2", manufacturers[0]), # 1
          Model(wheels[1], frames[2],  "M3", manufacturers[0]), # 2
          Model(wheels[0], frames[2],  "M4", manufacturers[1]), # 3
          Model(wheels[1], frames[3],  "M5", manufacturers[1]), # 4
          Model(wheels[2], frames[4],  "M6", manufacturers[1]), # 5
          Model(wheels[1], frames[4],  "M7", manufacturers[2]), # 6
          Model(wheels[2], frames[5],  "M8", manufacturers[2]), # 7
          Model(wheels[2], frames[6],  "M9", manufacturers[2])] # 8
if debug: 
    for i in models: i.describe()

""" Update Manufacturers with their bicycles """
for model in models:
    for manufacturer in manufacturers:
        if model.manufacturer.name == manufacturer.name:
            manufacturer.models.append(model)
if debug: 
    for i in manufacturers: i.describe()
    
# Experiments with inventory
x_bikes = [Bike(models[0], 2),
           Bike(models[1], 2),
           Bike(models[2], 1),
           Bike(models[3], 3)]
y_bikes = [Bike(models[3], 2),
           Bike(models[4], 2),
           Bike(models[5], 1),
           Bike(models[6], 3),
           Bike(models[7], 3)]
z_bikes = [Bike(models[5], 2),
           Bike(models[6], 2),
           Bike(models[7], 1),
           Bike(models[8], 3)]
if debug:
    for bike in x_bikes: bike.describe()
    for bike in y_bikes: bike.describe()
    for bike in z_bikes: bike.describe()

""" Shops """
shops = [Shop('X', 40, models[0:4], x_bikes),
         Shop('Y', 30, models[3:7], y_bikes),
         Shop('Z', 20, models[5:9], z_bikes)]
if debug: 
    for i in shops: i.describe()

""" Customers """
customers = [Customer('Aaron',  200),
             Customer('Barry',  500),
             Customer('Carla', 1000)]
if debug: 
    for i in customers: i.describe()  

""" The "Bicycle Industry" Assignment """

""" Shops with Inventory """
for shop in shops:
    print "Bicycle Shop " + shop.name + " carries the following bikes:"
    for bike in shop.bikes:
        cost = ((1.0*bike.model.cost) * (1.0 + (bike.model.manufacturer.percent/100.00))) * (1.0 + (shop.percent/100.00))
        print " > {} which weighs {} kg and costs ${} (Only {} Left)" .format(bike.model.name, str(bike.model.weight), cost, bike.quantity)
        
""" Customers and Options """
for customer in customers:
    print "Customer {} is looking for a bike under ${}." .format (customer.name, customer.cash)
    options = 0
    for shop in shops:
        for bike in shop.bikes:
            cost = ((1.0*bike.model.cost) * (1.0 + (bike.model.manufacturer.percent/100.00))) * (1.0 + (shop.percent/100.00))
            if cost <= customer.cash:
                #print " > They could get model {} from shop {} for ${}." .format (bike.model.name, shop.name, cost)
                options += 1
    #print " >> They have {} options." .format (options)
    choice = random.randint(1,options)
    #print " >> They choose option #{}." .format(choice)
    num = 0
    for shop in shops:
        for bike in shop.bikes:
            cost = ((1.0*bike.model.cost) * (1.0 + (bike.model.manufacturer.percent/100.0))) * (1.0 + (shop.percent/100.00))
            if cost <= customer.cash:
                num += 1
                if choice == num:
                    print " >>> {} decides to buy the {} from shop {} for ${}." .format(customer.name, bike.model.name, shop.name, cost)
                    customer.cash -= cost
                    print " >>>> and they still have ${} leftover." .format(customer.cash)
                    shop_cost = ((1.0*bike.model.cost) * (1.0 + (bike.model.manufacturer.percent/100.0)))
                    profit = cost - shop_cost
                    bike.quantity -= 1
                    print " >>>> Bike shop {} profited ${} and has {} model {} left." .format(shop.name, profit, bike.quantity, bike.model.name) 
    