# Create thread by extending thread class

# import thread module
from threading import *


# Extending thread class
class MyClass(Thread):

    # Target function for thread
    def run(self):
        for i in range(5):
            print("target func 1")


# Creating MyClass class object
MyObj = MyClass()

# Execution of target function
MyObj.start()

# Executed by main thread
for i in range(10):
    print('Main Thread')
