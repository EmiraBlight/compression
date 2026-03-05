from database import db

d = db("data/animals_small.txt")
print(d)
d.toBin("test")
