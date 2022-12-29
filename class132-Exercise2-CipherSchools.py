# define a function that takes list of strings
# list containing reverse of every string 

# note use list comprehension because we already did this exercise
# using normal method
# example 
# l = ['abc','xyz','tuv']
# reverse_string(l)---> ['bac','vut','zyx']

# solution 
def reverse_string(l):
    return [name[::-1]for name in l ]
print(reverse_string(['abc','xyz','tuv']))    


# or 
def reverse_string(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return(new_list)    