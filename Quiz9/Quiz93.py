import dbm
db1=dbm.open("Houses","c")

db1["item1.png"]="two bathrooms"
db1["item2.png"]="4 bedrooms"
db1["item3.png"]="3 floors"
db1["item4.png"]="a brick fireplace"
db1["item5.png"]="a basement and an attic"
db1["item6.png"]="open floor plan"


print(db1["item1.png"])
print(db1["item2.png"])
print(db1["item3.png"])
print(db1["item4.png"])
print(db1["item5.png"])
print(db1["item6.png"])
