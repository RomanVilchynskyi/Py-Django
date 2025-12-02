def my_filter(arr, func):
    result = []
    for i in arr:
        if func(i):   
            result.append(i)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = my_filter(numbers, lambda x: x % 2 == 0)
print("Even:", evens)

greater_5 = my_filter(numbers, lambda x: x > 5)
print("Greater than 5:", greater_5)

squares = my_filter(numbers, lambda x: x * x > 20)
print("Square > 20:", squares)


def outside_range(lst, start, end):
    for x in lst:
        if x < start or x > end:
            yield x

numbers = [1, 5, 10, 15, 20, 25]
start = 10
end = 20

result = list(outside_range(numbers, start, end))
print(result)  
