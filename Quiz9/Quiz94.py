import dbm
db1=dbm.open("Houses2","c")

db1["item1.png"]="two bathrooms"
db1["item2.png"]="4 bedrooms"
db1["item3.png"]="lots of windows"
db1["item4.png"]="a brick fireplace"
db1["item5.png"]="very large kitchen"
db1["item6.png"]="open floor plan"


print(db1["item1.png"])
print(db1["item2.png"])
print(db1["item3.png"])
print(db1["item4.png"])
print(db1["item5.png"])
print(db1["item6.png"])

for item in Houses2:
    print(item, Houses2[item])

Houses2.close()
