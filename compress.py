from database import db

d = db("data/animals_sorted.txt")
# print(d)
d.toBin("test")
d.getOrder()
print(d.compressOrder)
