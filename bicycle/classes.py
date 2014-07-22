class Wheel(object):
    """ This is Really Wheel Type """
    def __init__(self, weight, cost, model):
        self.weight = weight;
        self.cost = cost;
        self.model = model;
    def describe(self):
        print "The {} wheel weighs {} kg and costs ${}." .format(self.model, self.weight, self.cost)

class Frame(object):
    """ This is Really Frame Type """ 
    def __init__(self, weight, cost, material):
        self.weight = weight;
        self.cost = cost; 
        self.material = material; 
        self.name = self.material[0] + str(self.weight)
    def describe(self):
        print "The {} {} frame weighs {} kg and costs ${}." .format(self.name, self.material, self.weight, self.cost)
    
class Manufacturer(object):
    def __init__(self, name, models, percent):
        self.name = name
        self.models = models
        self.percent = percent
    def describe(self):
        print "The {} manufacturer sells {} model(s) at a profit of {}%." .format(self.name, len(self.models), self.percent)

class Model(object):
    """ This is a model of bike, so like Bicycle Type """
    def __init__(self, wheel, frame, name, manufacturer):
        self.wheel = wheel
        self.frame = frame
        self.name = name
        self.manufacturer = manufacturer
        self.cost = (wheel.cost * 2) + frame.cost
        self.weight = (wheel.weight * 2) + frame.weight
    def describe(self):
        print "The {} bicycle model by {} weights {} kg and costs ${}." .format(self.name, self.manufacturer.name, self.weight, self.cost)
        
class Bike(object):
    def __init__(self, model, quantity):
        self.model = model
        self.quantity = quantity  
    def describe(self):
        print "This inventory has {} model {}'s." .format (self.quantity, self.model.name)
        
class Shop(object):
    def __init__(self, name, percent, models, bikes):
        self.name = name
        self.percent = percent
        self.models = models
        self.bikes = bikes
    def describe(self):
        print "The {} shop sells {} model(s) at a profit of {}%." .format(self.name, len(self.models), self.percent)
        
class Customer(object):
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
    def describe(self):
        print "{} the customer has ${} to spend on a bicycle." .format(self.name, self.cash)
        