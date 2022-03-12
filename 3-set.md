**III-Set**

1. Definition 

A set is a data structure that can store any number of unique values in any order. Sets are different from arrays in the sense that they only allow non-repeated, unique values within them.

2. Implementing 

Lets see deferrence between an array and a set:


```
>>> an_array = [1,2,2,3,3,4] # repeated values
>>> a_set = set(an_array) # non-repeated, unique values
>>> a_set
{1, 2, 3, 4}

```
In this example, we can see that the numbers in the array can be repeated while they cannot in the set.

This can also be used for strings:

```
>>> a_string = "my name is Fulgence Dalo"
>>> a_set = set(a_string)
>>> a_set
{'m', ' ', 'y', 'n', 'a', 'i', 's', 'F', 'u', 'l', 'g', 'e', 'c', 'D', 'o'}
```
Here we can see that when implementing the set, the letters are not repeatred.

We can use the "add(value)" to add a value to a set and "remove(value)" to remove a value from a set.

* Performance



*  [Problem](set-problem.py)

Try the problem first before looking at the solution

* [Solution](set-solution.py)









