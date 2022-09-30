def mean(*numbers):
    if not numbers:
        return None
    return sum(numbers)/len(numbers)

print(mean(1,2,3,4))
print(mean(1,22,1,1,3,1,234,321,1,345,312))
print(mean())