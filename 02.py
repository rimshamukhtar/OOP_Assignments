# 2. Using cls

# Assignment:

# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.

class Counter():
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print(f"Total Objects created: {cls.count}")

#  Creating objects

c1 = Counter()
c2 = Counter()
c3 = Counter()

# Calling class method
Counter.show_count()