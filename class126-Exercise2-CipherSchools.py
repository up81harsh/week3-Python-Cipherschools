# user = {
#     "name"="Harshit"
#     "age" = 24
#     "fav_movies":['coco','avengers']
#     'fav_songs' : ['song1','song2']
# }

# solution
user ={}
name = input("enter your name :")
age = int(input("what is your age : "))
fav_movies =input("your favourite movies : ").split(",")
fav_songs = input("your fav songs : ").split(",")

user['name'] = name
user['age']= age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
#print(user)

for key , value in user.items():
    print(f"{key}: {value}")