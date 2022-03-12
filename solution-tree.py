"""CSE212 
Kouadio Kouao - BYU-I
Set-problem 
"""
# This Python program insert data 
# into a BTS. It inserts the smaller 
# values to the left and larger to 
# the right and prints them.
  
class BTS:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent 
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BTS(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BTS(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = BTS(12)
root.insert(6)
root.insert(14)
root.insert(3)

root.PrintTree()