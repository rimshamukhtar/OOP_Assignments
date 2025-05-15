# 3. Public Variables and Methods

# Assignment:
# Create a class Car with a public variable brand and a public method start().
#  Instantiate the class and access both from outside the class.

class Car():
    
    def __init__(self, brand):
        self.brand = brand     

    def start(self):
        print(f"{self.brand} is starting...")  

#  create object
car1 = Car("Honda")

#  access public variable
print("Brand:", car1.brand)

#  call public method
car1.start()

        


