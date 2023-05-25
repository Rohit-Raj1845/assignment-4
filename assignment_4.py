QUESTION:-1. Create a python program to sort the given list of tuples based an integer value using a lambda function.
[('Sachin Tendulkar',34357),('Ricky Ponting',27483),('Jack Kallis',25534),('Virat Kohli',24936)]
cricket_score = [('Sachin Tendulkar',34357),('Ricky Ponting',27483),('Jack Kallis',25534),('Virat Kohli',24936)]
print("Original List of Tuples:")
print(cricket_score)
cricket_score.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(cricket_score)



QUESTION:-2. Write a python program to find the squares of all the numbers in the given list of integers using lambda and map functions.
l = [1,2,3,4,5,6,7,8,9,10]
def sq(x): 
    return x**2
print(list(map(sq,l)))
print(list(map(lambda x : x**2 , l)))



QUESTION:-3. Write a python program to convert the given of integers into a tuple of strings. use map and lambda functions.
Given String:[1,2,3,4,5,6,7,8,9,10]
Expected Output:('1','2','3','4','5','6','7','8','9','10')

nums_list = [1,2,3,4,5,6,7,8,9,10]
result_list = tuple(map(lambda x: str(x), [1,2,3,4,5,6,7,8,9,10]))
print(result_list)



QUESTION:-4. Write a python program using reduce function to compute the product of a list containing numbers from 1 to 25.

from functools import reduce
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(reduce(lambda x,y : x*y , l))



QUESTION:-5. Write a python program to filter the numbers in a given list that are divisible by 2 and 3 using the filter function.
[2,3,6,9,27,60,90,120,55,46]
l1 = [2,3,6,9,27,60,90,120,55,46]
print(list(filter(lambda x : x%2 == 0 and x%3 == 0 , l1)))



QUESTION:-6. Write a python program to find palindromes in the given list of strings using lambda and filter function.
['python','php','aba','radar','level']
texts = ['python','php','aba','radar','level']
print("Original list of strings:")
print(texts)
result = list(filter(lambda x : (x == "".join(reversed(x))), texts))
print("\nList of Palindromes:")
print(result)
