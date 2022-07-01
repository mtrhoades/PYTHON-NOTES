# Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.

unsorted_list_of_tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 

# print(unsorted_list_of_tuples[0][1])

sorted_list_of_tuples = sorted(unsorted_list_of_tuples ,key=lambda x: x[1])

print(sorted_list_of_tuples)
# Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


# Write a lambda function to cube every element of a list.
# Original list: [3,6,9,2] List after lambda function: [27,216,729,8]

my_list = [3, 6, 9, 2]
cubed_list = lambda x : [num**3 for num in x]

print(cubed_list(my_list))


# Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.
# Input list: [3,6,9,2] 
# List after lambda function and list comprehension: [False, True, False, True]
oddOrEven = lambda x : True if x % 2 == 0 else False
boolean_list = [oddOrEven(num) for num in my_list]

print(boolean_list)

# Use a list comprehension to create a list of the numbers from 1 to 100 (including 100).


# Use a dictionary comprehension to count the length of each word in a sentence.
# Input: "The quick brown fox jumped over the fence." otuput: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}

