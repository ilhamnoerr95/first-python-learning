# statement if in python, elif (else if) kegunaan elif ini apabila memiliki kondisi yg 
# sudah terpenuhi maka elif yg lain tidak akan di eksekusi bisa dikatakan menjadi 1 blok ,and else
# author: irahama
# date: 2014-07-13

num = -1
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")
print("end of if statement")

print("Pilih menu [1-3] kamu:")
a = input()

if a == "1":
    print("ini menu 1")
elif a == "2":
    print("ini menu 2")
elif a == "3":
    print("ini menu 3")
else:
    print("ini menu lain")