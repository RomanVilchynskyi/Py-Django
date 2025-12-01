# task 1.1
# bd = int(input("Enter your bithdate: "))

# def age(bd, year) -> int:
#     return year - bd

# print(age(bd, 2025))

# task 1.2
# gb = int(input("Enter file size in gb: "))

# mb = gb * 1024

# # Розмір одного файлу
# file_size = 820  # МБ

# # Кількість файлів, які помістяться
# count = int(mb // file_size)

# print("На флешку поміститься", count, "файлів розміром 820 МБ.")

# task 2.1
# num = input("Enter number from 0 to 9: ")

# match num:
#     case "1": print("!")
#     case "2": print("@")
#     case "3": print("#")
#     case "4": print("$")
#     case "5": print("%")
#     case "6": print("^")
#     case "7": print("&")
#     case "8": print("*")
#     case "9": print("(")
#     case "0": print(")")
#     case _: print("Invalid number")

# task 2.2
# year = int(input("Enter year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not leap year")

# task 2.3
# day = int(input("Enter day: "))
# month = int(input("Enter month: "))
# year = int(input("Enter year: "))

# def is_leap(year):
#     return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# days_in_month = [31, 29 if is_leap(year) else 28, 31, 30,
#                  31, 30, 31, 31, 30, 31, 30, 31]

# day += 1

# if day > days_in_month[month - 1]:
#     day = 1
#     month += 1

# if month > 12:
#     month = 1
#     year += 1

# print(f"Наступна дата: {day:02d}.{month:02d}.{year}")

#task 3.1

# start = int(input("Input start: "))
# end = int(input("Input end: "))

# s = 0
# for i in range(start, end + 1):
#     s += i

# print("Sum:", s)

#task 3.2

# num = input("Enter number: ")
# print("Total digits:", len(num))

#task 3.3

# positive = 0
# negative = 0
# zeros = 0

# even = 0
# odd = 0

# for _ in range(10):            
#     num = int(input("Enter numbers: "))

#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
#     else:
#         zeros += 1

#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1


# print("\n--- Stats ---")
# print("positive:", positive)
# print("negative:", negative)
# print("zeros:", zeros)
# print("even:", even)
# print("odd:", odd)

#task 3.4
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

index = 0

while True:
    print("Today:", days[index])
    choice = input("You wanna see the next day? (y/n): ").lower()
    if choice != "y":
        break
    index = (index + 1) % len(days)