thisset={"apple","banana","cherry"}
thisset.add("kiwi")
print(thisset)

#update

thisset={"apple","banana","kiwi"}
myset={"cherry","orange","mango"}
thisset.update(myset)
print(thisset)

thisset={"apple","banana","kiwi"}
myset=["cherry","orange","mango"]
thisset.update(myset)
print(thisset)

