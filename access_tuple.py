#access tuple item

thistuple=("apple","banana","kiwi","orange","mango","watermelon")
print(thistuple[3])

#nagative 

thistuple=("apple","banana","kiwi","orange","mango","watermelon")
print(thistuple[-1])

#range

thistuple=("apple","banana","kiwi","orange","mango","watermelon")
print(thistuple[2:5])

#nagative range

thistuple=("apple","banana","kiwi","orange","mango","watermelon")
print(thistuple[-4:-1])

# leaving out the start value

thistuple=("apple","banana","kiwi","orange","mango","watermelon")
print(thistuple[:4])

#leaving out the end of the value
thistuple=("apple","banana","kiwi","orange","mango","watermelon")
print(thistuple[3:])

#if condition

thistuple=("apple","banana","kiwi","orange","mango","watermelon")
if "apple" in thistuple:
            print("yes apple is  in the fruits tuple")


