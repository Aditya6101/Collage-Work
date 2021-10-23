# Create Thread without extending Thread Class

# Importing thread module
from threading import *


class MyClass():

    # Creating Instance Method
    def display(self):
        for i in range(10):
            print("Child Thread")


# Creating object of MyClass
MyObj = MyClass()

# Creating object of thread by targeting instance method of MyClass class
ThreadObj = Thread(target=MyObj.display())

ThreadObj.start()

# for loop executed by main thread
for i in range(10):
    print('Main Thread')
