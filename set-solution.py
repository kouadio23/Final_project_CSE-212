"""CSE212 
Kouadio Kouao - BYU-I
Set-problem 
"""

# This Python program is to check 
# if two lists have at-least 
# one element in common
# using set and property
  
def common_element(a, b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True 
    else:
        return False
          
  
a = {1, 2, 3, 4, 5}
b = {5, 6, 7, 8, 9}
print(common_element(a, b))  # Should show True
  
a ={1, 2, 3, 4, 5}
b ={6, 7, 8, 9}
print(common_element(a, b)) #  Should show False