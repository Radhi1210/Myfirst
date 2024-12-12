thisdict={"name" : "aesha","lastname"  : "mavani","age" : 22}
x=thisdict["name"]
print(x)

thisdict={
"name" : "aesha","lastname"  : "mavani","age" : 2}
x=thisdict.get("name")
print(x)

#get keys ()

thisdict={"name" : "aesha","lastname"  : "mavani","age" : 22}
x=thisdict.keys()
print(x)

#key update

thisdict={"name" : "aesha","lastname"  : "mavani","age" : 22}
x=thisdict.keys()
print(x)
thisdict["gender"]="female"
print(x)


#get values

thisdict={"name" : "aesha","lastname"  : "mavani","age" : 22}
x=thisdict.values()
print(x)


#update values

thisdict={"name" : "aesha","lastname"  : "mavani","age" : 22}
x= thisdict.values()
print(x)
thisdict["gender"]="female"
print(x)

#changes original values
thisdict={"name" : "aesha","lastname"  : "mavani","age" : 22}
x=thisdict.values()
print(x)
thisdict["age"]=21
print(x)


# get items

thisdict={"name" : "aesha","lastname"  : "mavani","age" : 22}
x=thisdict.items()
print(x)

#get change itemns

thisdict={"name" : "aesha","lastname"  : "mavani","age" : 22}
x=thisdict.items()
thisdict["age"]=21
print(x)


#get add a items

thisdict={"name" : "aesha","lastname"  : "mavani","age" : 22}
x=thisdict.items()
print(x)
thisdict["gender"]="female"
print(x)

#check if key exist

thisdict={"name" : "aesha","lastname"  : "mavani","age" : 22}
if "age" in thisdict:
 print("yes ,  age is one of the key is exists in  this dict ")