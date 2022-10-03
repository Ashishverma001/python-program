class cat:

    # Constructor
    def __init__(self, name, age, breed):
        # Syntax for instance variable
        # Self.<attribute> = <parameter>
        self.name = name
        self.age = age
        self.breed = breed

cat1 = cat('soni', 3, 'persian')
cat2 = cat('mia', 4,'siamese')
cat3 = cat('molly', 5, 'Egyptian mau')

print(cat1.name, cat1.age, cat1.breed)
print(cat2.name, cat2.age, cat2.breed)
print(cat3.name, cat3.age, cat3.breed)