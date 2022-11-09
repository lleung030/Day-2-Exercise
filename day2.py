# ## Exercise 1 
# Given a list as a parameter,write a function that returns a list of numbers that are less than ten
# For example: Say your input parameter to the function is [1,11,14,5,8,9]...Your output should [1,5,8,9]


def less_than_10(lst):
    recipe=[]
    for i in range(len(lst)):
        if lst[i]<10:
            recipe.append(lst[i])
    return recipe
    

print(less_than_10([1,11,14,5,8,9]))

# Exercise 2 
# Write a function that takes in two lists and returns the two lists merged together and sorted
# Hint: You can use the .sort() method

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def sorting(a,b):

    a.sort()
    b.sort()
    
    return a+b
    
print(sorting(l_1,l_2))


