# Create a Thread without using an Explicit function

# Import required modules
from threading import *


# Explicit function
def display():
    for i in range(10):
        print("Child Thread")

# Create object of thread class
ThreadObj = Thread(target=display)

# Executing child thread
ThreadObj.start()

# Executing main thread
for i in range(10):
    print('Main Thread')
