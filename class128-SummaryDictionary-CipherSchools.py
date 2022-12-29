# summary dictionary
# what is dictionary
# unordered collection of data 
d = {"name" : "harshit", "age ": 24}

# or 

d1 = dict(name ="harshit" ,"age "= 24)

#or 

d2 = {
    "name ": "harshit",
    "age": 24,
    "fav_movies": []
}

# how to access data from dictionary
# you cannot do like 
# d[0] , because there is no order inside dictionary
 

#syntax
# print(dictname[keyname])
# print(d['name])

# add data inside empty dict
empty_dict = {}
empty_dict['key1']='value1'
empty_dict['key2']='value2'
print(empty_dict)

#check existence of values inside dict 
# use in keyword to check for keys 
if 'name' in d :

# how to iterate in dictionary :
# most common method :
for key , value in d.items():
    print(f'key is {key} and value is {value}' )

# to print all keys  
for i in d:
    print(i)

# to print all values:
for i in d.values():
    print(i)

# most common dict methods

# get method
# to acess a key and check existence
print(d.get('name'))

# ques - why we use get 
# ans - to get rid of error 
#example
print(d['name'])           # error
print(d.get('names'))      # none

# to delete a item
# pop ---> take one arguement which is keyname 

popped = d.pop('name')
print(popped)

# popitem 
popped = d.popitem()
print(popped)
print(d)