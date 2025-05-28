# make program use for-loop, list and range

banyak = int(input("how many data? "))

name = []
umur = []


for i in range(banyak):
    print(f"Data ke {i}")
    name.append(input("name: "))
    umur.append(int(input("umur: ")))

for a in range(0, len(name)): 
    data_name = name[a]
    data_umur = umur[a]
    print(f"{data_name} berumur {data_umur}")

