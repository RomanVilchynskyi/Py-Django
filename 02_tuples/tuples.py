# task 1
arr = [3, 14, 1, 25, 9, 100]

newArr = []
for i in arr:
    if(i > 10):
        newArr.append(i)

print(newArr)

# task 2

fruites = ['apple', 'banana', 'apple', 'orange', 'apple']

counter = fruites.count("apple")

print(counter)

# task 3

firstSet = {1, 2, 3}
secSet = {3, 4, 5}

print(f"unique: {firstSet.symmetric_difference(secSet)}")

# task 4

cort = [(1, 5), (2, 1), (3, 4)]

res = sorted(cort, key=lambda x: x[1])

print(res)

# task 5

print("=======================")
nested = [[1, 2], [3, 4, 5], [6]]

flat = sum(nested, [])

print(flat)

# task 6

string = "hello world hello python world"

words = string.split()
freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

print(freq)
