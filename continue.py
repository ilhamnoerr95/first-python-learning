# learn continue: for skip process and repeat to the next iteration

print("This is the start of the program.")
for i in range(1, 31):
    if i % 2 == 0:
        continue # when the value is even, skip the following code, n repeat to the next iteration
    print(i) # only print data with odd value
print("This is the end of the program.")