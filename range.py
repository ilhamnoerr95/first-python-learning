# range() function
# range(start, stop, step)
# range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(1, 10) = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# range(1, 10, 2) = [1, 3, 5, 7, 9] = 1 + 2 = 3 + 2 = 5 + 2 = 7 + 2 = 9
# range(10, 1, -1) = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

number = range(1,10, 3)

for no in number: 
    print(no)