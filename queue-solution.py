"""CSE212 
Kouadio Kouao - BYU-I
queue-problem 
"""
class Queue:

    """ this fuction initialises the class queue"""
    def __init__(self):
        self.fruits = []

    """This function checks is the list is empty"""
    def isEmpty(self):
        return self.fruits == []

    """This function enqueue in the list"""
    def enqueue(self, fruits):
        self.fruits.insert(0, fruits)

    """This function dequeues from the list"""
    def dequeue(self):
        return self.fruits.pop()

        

# problem 1
# write a function to enqueue 4 fruits in the list and print the list.
# your code goes here.
new = Queue()
new.enqueue("banana")
new.enqueue("apple")
new.enqueue("mango")
new.enqueue("orange")
print(new)

print('=================================')

# problem 2
# write a funtion to dequeue the first fruits from the list.
# your code goes here.
new = Queue()
new.enqueue("banana")
new.enqueue("apple")
new.enqueue("mango")
new.enqueue("orange")
old = new.dequeue()
print(old) # should print "banana"


