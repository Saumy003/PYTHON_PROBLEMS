# Itration Key Values in Dictonary

my_dict = {
    "name" : "Anirudh",
    "age" : 22,
    "gender" : "Male"
}

for k in my_dict.keys():
    print(my_dict[k])
# both will print same things
for v in my_dict.values():
    print(v)

# print output like this: name -> Anirudh
for k ,v in my_dict.items():
    print(f"{k} -> {v}")
    